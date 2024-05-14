from selenium.webdriver.common.by import By

type_name = [By.CSS_SELECTOR,
                 ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(1) > .el-form-item__content > .el-col > .el-input > input"]
type_category = [By.ID, "select_add_class_bug"]
type_brand = [By.ID, "select_add_brand_bug"]
type_unit = [By.CSS_SELECTOR, ".el-input.el-input--medium.el-input--suffix > input"]
type_unit_ul = [By.CLASS_NAME, "el-select-dropdown__item"]
type_purchase = [By.CSS_SELECTOR,
                 ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(5) > .el-form-item__content > .el-col > .el-input > input"]
type_sale = [By.CSS_SELECTOR,
             ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(6) > .el-form-item__content > .el-col > .el-input > input"]
type_file = [By.NAME, "file"]
type_saveNew = [By.CSS_SELECTOR, ".el-dialog__body + .el-dialog__footer > .dialog-footer > button:nth-child(2) > span"]
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
