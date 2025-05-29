import os
import time
from typing import Optional

from core.logger import get_logger
from voice.recognition.providers.selenium_stt.provider import SeleniumSTTProvider

logger = get_logger(__name__)

if __name__ == "__main__":
    provider = None
    try:
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html_file_name = "index.html"
        html_file_path = os.path.join(script_dir, "assets", html_file_name)

        if not os.path.exists(html_file_path):
            logger.error(f"[FATAL ERROR] {html_file_name} not found at: {html_file_path}")
            logger.error(f"Please ensure '{html_file_name}' is in the '{os.path.join(script_dir, 'assets')}' directory.")
            exit(1)
        
        target_website_path = html_file_path
        
        logger.info(f"[INFO] Using speech recognition source: {target_website_path}")

        provider = SeleniumSTTProvider(
            website_path=target_website_path, 
            language="en-US", 
            quiet_timeout_seconds=7.0 
        )
        
        print("Made By ❤️ @DevsDoCode (SeleniumSTTProvider Test)")
        
        consecutive_error_count = 0
        max_consecutive_errors = 3

        while True: 
            if not provider or not provider.driver_manager.driver:
                logger.error("[ERROR] Speech listener or its WebDriver is not properly initialized. Attempting to re-initialize.")
                try:
                    provider = SeleniumSTTProvider(
                        website_path=target_website_path, 
                        language="en-US", 
                        quiet_timeout_seconds=7.0
                    )
                    logger.info("Re-initialized provider successfully.")
                    consecutive_error_count = 0
                except Exception as e:
                    logger.error(f"Failed to re-initialize provider: {e}")
                    consecutive_error_count +=1
                    if consecutive_error_count >= max_consecutive_errors:
                        logger.error("Max consecutive initialization errors reached. Exiting.")
                        break
                    time.sleep(2)
                    continue
            
            print("\nReady to listen...") 
            speech = provider.listen(prints=True)

            if speech is None:
                print("A critical error occurred during listen. Listener might try to recover.")
                consecutive_error_count += 1
                if consecutive_error_count >= max_consecutive_errors:
                    logger.error("Max consecutive listening errors reached. Exiting.")
                    break
                time.sleep(1)
                continue

            consecutive_error_count = 0

            if speech == "":
                print("No speech detected in this attempt or quiet timeout.") 
            else:
                print(f"Final text processed by main test: {speech}") 
                if "exit listener" in speech.lower():
                     print("Exit command received. Shutting down listener test.")
                     break
            
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Shutting down listener test...")
    except Exception as e:
        logger.error(f"[FATAL ERROR] An unexpected error occurred in the main application loop: {e}", exc_info=True)
    finally:
        print("Cleaning up resources...")
        if provider:
            pass 
        print("Listener test application finished.")
