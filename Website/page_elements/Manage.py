from selenium.webdriver.common.by import By

type_Manage = [By.LINK_TEXT, "商品管理"]
type_new = [By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[2]/div[3]/button"]
type_add_name = [By.CSS_SELECTOR,
                 ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(1) > .el-form-item__content > .el-col > .el-input > input"]
type_add_category = [By.ID, "select_add_class_bug"]
type_add_brand = [By.ID, "select_add_brand_bug"]
type_unit = [By.CSS_SELECTOR, ".el-input.el-input--medium.el-input--suffix > input"]
type_unit_ul = [By.CLASS_NAME, "el-select-dropdown__item"]
type_purchase = [By.CSS_SELECTOR,
                 ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(5) > .el-form-item__content > .el-col > .el-input > input"]
type_sale = [By.CSS_SELECTOR,
             ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(6) > .el-form-item__content > .el-col > .el-input > input"]
type_file = [By.NAME, "file"]
type_save = [By.CSS_SELECTOR, ".el-dialog__body + .el-dialog__footer > .dialog-footer > button:nth-child(1)"]
type_saveNew = [By.CSS_SELECTOR, ".el-dialog__body + .el-dialog__footer > .dialog-footer > button:nth-child(2)"]
type_cancel = [By.CSS_SELECTOR, ".el-dialog__body + .el-dialog__footer > .dialog-footer > button:nth-child(3)"]
type_query_Name = [By.ID, "product_name"]
type_query_category = [By.ID, "select_class_bug"]
type_query_brand = [By.ID, "select_brand_bug"]
type_status = [By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[1]/form/div[4]/div/div/div[1]/input"]
type_status_ul = [By.CLASS_NAME, "el-select-dropdown__item"]
type_create_start_date = [By.CSS_SELECTOR,
                          "#app > div > div.main-container.hasTagsView > section > div > div.j-form > form > div:nth-child(5) > div > div > input:nth-child(2)"]
type_create_end_date = [By.CSS_SELECTOR,
                        "#app > div > div.main-container.hasTagsView > section > div > div.j-form > form > div:nth-child(5) > div > div > input:nth-child(4)"]
type_modify_start_date = [By.CSS_SELECTOR,
                          "#app > div > div.main-container.hasTagsView > section > div > div.j-form > form > div:nth-child(6) > div > div > input:nth-child(2)"]
type_modify_end_date = [By.CSS_SELECTOR,
                        "#app > div > div.main-container.hasTagsView > section > div > div.j-form > form > div:nth-child(6) > div > div > input:nth-child(4)"]
type_query_button = [By.ID, "product_query"]
type_reset_button = [By.CSS_SELECTOR,
                     "#app > div > div.main-container.hasTagsView > section > div > div.mb8.el-row > div:nth-child(2) > button"]
type_data_modify_start = [By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[3]/div[4]/div[2]/table/tbody/tr["]
type_data_modify_end = [By.XPATH, "]/td[13]/div/button[1]"]
type_date_disable_open_start = [By.XPATH,
                                "/html/body/div[1]/div/div[2]/section/div/div[3]/div[4]/div[2]/table/tbody/tr["]
type_date_disable_open_end = [By.XPATH, "]/td[13]/div/button[2]"]
