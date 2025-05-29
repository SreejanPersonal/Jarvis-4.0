from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from core.logger import get_logger

logger = get_logger(__name__)

class LanguageHandler:
    def __init__(self, provider):
        self.provider = provider
    
    def select_language(self) -> None:
        if not self.provider.driver_manager.driver:
            return
        self.provider.driver_manager.driver.execute_script(
            f"""
            var select = document.getElementById('language_select');
            select.value = '{self.provider.language}';
            var event = new Event('change');
            select.dispatchEvent(event);
            """
        )

    def verify_language_selection(self) -> bool:
        if not self.provider.driver_manager.driver or not self.provider.driver_manager.wait:
            return False
        try:
            language_select = self.provider.driver_manager.wait.until(
                EC.presence_of_element_located((By.ID, "language_select"))
            )
            self.provider.driver_manager.wait.until(
                lambda driver: driver.find_element(
                    By.CSS_SELECTOR, 
                    f"#language_select option[value='{self.provider.language}']"
                ).is_selected()
            )
            selected_option = language_select.find_element(By.CSS_SELECTOR, "option:checked")
            selected_language_value = selected_option.get_attribute("value")
            return selected_language_value == self.provider.language
        except Exception:
            return False
