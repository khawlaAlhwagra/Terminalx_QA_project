from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


class RemoveFavoriteTerminalx(BasePage):
    """
    Page Object for interacting with the Favorites (Wishlist) section.
    This class provides helpers to open the favorites section, count items,
    and remove the first favorite item.
    """

    # Generic locators – kept flexible per request
    FAVORITES_LINK = '//*[contains(@href, "wishlist") or contains(@href, "favorites") or contains(@class, "favorites") or @id="favorites" or @data-qa="favorites"]'
    FAVORITE_ITEMS = '//*[contains(@class, "wishlist") or contains(@class, "favorites")]//*[contains(@class, "item") or contains(@class, "product") or contains(@data-qa, "wishlist-item")]'
    REMOVE_ICON_RELATIVE = './/*[contains(@class, "remove") or contains(@data-action, "remove") or contains(@aria-label, "Remove") or contains(@class, "delete")]'
    # Common loader overlay seen on site
    LOADER_OVERLAY = '//*[contains(@class, "loader") or contains(@class, "loading") or contains(@class, "loader-container")]'

    def __init__(self, browser):
        super().__init__(browser)
        self._wait = WebDriverWait(self._browser, 15)

    def _wait_for_loader_clear(self, timeout: int = 10):
        """Best-effort wait for any loader overlay to disappear."""
        try:
            WebDriverWait(self._browser, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, self.LOADER_OVERLAY))
            )
        except Exception:
            pass

    def _get_favorite_items(self):
        """Return current favorite item WebElements without blocking on presence."""
        return self._browser.find_elements(By.XPATH, self.FAVORITE_ITEMS)

    def open_favorites_section(self):
        """Open the favorites/wishlist section by clicking a header link or fallback to a direct URL."""
        try:
            # Ensure potential loaders are not covering the UI
            self._wait_for_loader_clear(10)

            link = self._wait.until(EC.element_to_be_clickable((By.XPATH, self.FAVORITES_LINK)))
            try:
                link.click()
            except Exception:
                # Fallback to JS click if intercepted
                self._browser.execute_script("arguments[0].click();", link)

            # Wait for navigation or content load
            try:
                WebDriverWait(self._browser, 10).until(
                    lambda d: "/wishlist" in d.current_url or "/favorites" in d.current_url
                )
            except Exception:
                pass
        except TimeoutException:
            # Fallback: try navigating directly to a probable wishlist URL
            try:
                self._browser.get("https://www.terminalx.com/wishlist")
            except Exception:
                # As a last resort, try a generic favorites path
                self._browser.get("https://www.terminalx.com/favorites")

    def count_favorites(self) -> int:
        """Return the number of favorite items currently visible."""
        # Do not block on presence here — it can cause hangs when list becomes empty
        self._wait_for_loader_clear(5)
        items = self._get_favorite_items()
        return len(items)

    def remove_first_favorite(self) -> bool:
        """
        Remove the first favorite item found.
        Returns True if a removal action was attempted and list size appears to change; False otherwise.
        """
        before = self.count_favorites()
        if before == 0:
            return False

        # Get first item and click its remove icon (or similar actionable control)
        items = self._get_favorite_items()
        first = items[0]

        # Ensure the item is visible and hovered (some UIs reveal remove on hover)
        try:
            self._browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", first)
        except Exception:
            pass
        try:
            ActionChains(self._browser).move_to_element(first).pause(0.2).perform()
        except Exception:
            pass

        # Try multiple candidate selectors for remove within the item
        candidate_xpaths = [
            self.REMOVE_ICON_RELATIVE,
            './/*[contains(@data-test-id, "remove") or contains(@data-testid, "remove")]',
            './/*[contains(@class, "wishlist-remove") or contains(@class, "remove-from-wishlist")]',
            './/*[contains(@class, "filled-heart") or contains(@class, "heart") and contains(@class, "active")]',
            './/*[contains(@aria-label, "Remove") or contains(@aria-label, "remove") or contains(@aria-label, "הסר")]',
            './/button[contains(@class, "remove") or contains(@data-action, "remove")]',
        ]

        remove_btn = None
        for xp in candidate_xpaths:
            try:
                el = first.find_element(By.XPATH, xp)
                remove_btn = el
                break
            except Exception:
                continue

        # If we still couldn't find a remove inside item, attempt a broader toggle within wishlist context
        if remove_btn is None:
            try:
                remove_btn = self._browser.find_element(By.XPATH, '//*[contains(@class, "wishlist") or contains(@id, "wishlist")]//*[contains(@class, "remove") or contains(@data-action, "remove") or contains(@aria-label, "Remove") or contains(@class, "heart")]')
            except Exception:
                remove_btn = None

        if remove_btn is None:
            return False

        # Try to click the remove button
        try:
            remove_btn.click()
        except Exception:
            try:
                self._browser.execute_script("arguments[0].click();", remove_btn)
            except Exception:
                return False

        # Wait for the item to be removed or count to decrease using non-blocking polling
        self._wait_for_loader_clear(10)
        try:
            WebDriverWait(self._browser, 10).until(lambda d: len(self._get_favorite_items()) < before)
            return True
        except Exception:
            # Fallback: staleness of the former first item or invisibility
            try:
                self._wait.until(EC.staleness_of(first))
                return True
            except (TimeoutException, StaleElementReferenceException):
                try:
                    WebDriverWait(self._browser, 5).until(lambda d: len(self._get_favorite_items()) < before)
                    return True
                except Exception:
                    return False

