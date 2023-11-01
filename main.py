from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    # Set up the headless browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the page
        driver.get('https://farrukh1068.cloudflareaccess.com/warp')

        # Fill out the email field
        email_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/div[1]/input[1]')
        email_field.send_keys('fabbasi@adapture.com')
        time.sleep(5)
        # Submit the email form (assuming there's a submit button)
        submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/div[2]/button')
        submit_button.click()

        # Wait for a moment to ensure the form submission completes
        time.sleep(5)

        # Ask the user for the verification code
        verification_code = input("Enter the verification code: ")

        # Fill out the verification code field (assuming the field name is 'verification_code')
        verification_code_field = driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div/div[1]/div[2]/form/div[1]/input[1]')
        verification_code_field.send_keys(verification_code)

        # Submit the verification code form (assuming there's a submit button)
        submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/form/div[2]/div/button')
        submit_button.click()

        # Wait for a moment to ensure the form submission completes
        time.sleep(5)

    finally:
        # Close the browser
        driver.quit()


if __name__ == '__main__':
    main()
