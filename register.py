#/usr/bin/python
import sys
import os
import time
from selenium import webdriver

p = '/tmp/idx'


def get_cur_idx():
    mode = 'r+' if os.path.exists(p) else 'w+'
    with open(p, mode) as f:
        data = f.read()
        idx = int(data) if data else 1000
        idx += 1
        f.seek(0)
        f.write(str(idx))
    return idx


def fill_form(email='ads8810', loop=1):
    try:
        driver = webdriver.Chrome('/Users/Jonathan/Documents/chromedriver')
    except:
        raise ValueError("Cannot open browser")
    for i in range(loop):
        try:
            idx = get_cur_idx()
            # open browser
            # go to webpage
            driver.get('https://www.wecantryit.com')
            # click on REGISTER
            driver.find_element_by_link_text('REGISTER').click()
            # fill form
            form_info = (
                ('xoo_el_reg_email', email + '+{idx}@gmail.com'),
                ('xoo_el_reg_fname', 'Jonathan_{idx}'),
                ('xoo_el_reg_lname', 'Tam'),
                ('xoo_el_reg_pass', '123456'),
                ('xoo_el_reg_pass_again', '123456')
            )
            for tag_name, info in form_info:
                if 'email' in tag_name or 'fname' in tag_name:
                    info = info.format(idx=idx)
                driver.find_element_by_name(tag_name).clear()
                driver.find_element_by_name(tag_name).send_keys(info)
            # accept term
            driver.find_element_by_name('xoo_el_reg_terms').click()
            # submit
            driver.find_element_by_xpath('//button[text()="Sign Up"]').click()
            # driver.close()
            time.sleep(1)
            driver.find_element_by_link_text('Logout').click()
        except Exception as e:
            print e
            with open(p, 'w+') as f:
                f.seek(0)
                f.write(str(idx - 1))
            driver.close()
    return None





if __name__ == '__main__':
    fill_form(email='ads8810')
    sys.exit('DONE!!!')
