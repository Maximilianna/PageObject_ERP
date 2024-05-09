from selenium.webdriver.common.by import By

type_Spgl = [By.LINK_TEXT, "商品管理"]
type_new = [By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[2]/div[3]/button"]
type_add_name = [By.CSS_SELECTOR,
                 ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(1) > .el-form-item__content > .el-col > .el-input > input"]
type_add_class = [By.ID, "select_add_class_bug"]
type_add_brand = [By.ID, "select_add_brand_bug"]
type_unit = [By.XPATH, "/html/body/div[2]/div/div[2]/form/div[4]/div/div[1]/div/div/input"]
type_unit_ul = [By.CSS_SELECTOR,
                "body > div:nth-child(10) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul"]
type_unit_li = [By.XPATH, "li"]
type_purchase = [By.CSS_SELECTOR,
                 ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(5) > .el-form-item__content > .el-col > .el-input > input"]
type_sale = [By.CSS_SELECTOR,
             ".el-dialog > .el-dialog__body > .el-form > .el-form-item:nth-child(6) > .el-form-item__content > .el-col > .el-input > input"]
type_file = [By.NAME, "file"]
type_save = [By.XPATH, "/html/body/div[4]/div/div[3]/div/button[1]/span"]
type_saveNew = [By.XPATH, "/html/body/div[4]/div/div[3]/div/button[2]/span"]
type_cancel = [By.XPATH, "/html/body/div[2]/div/div[3]/div/button[3]/span"]
type_query_Name = [By.ID, "product_name"]
type_query_class = [By.ID, "select_class_bug"]
type_query_brand = [By.ID, "select_brand_bug"]
type_status = [By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[1]/form/div[4]/div/div/div[1]/input"]
type_status_ul = [By.CSS_SELECTOR,
                  "body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul"]
type_status_li = [By.XPATH, "li"]
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
type_records = [By.CSS_SELECTOR,
                "#app > div > div.main-container.hasTagsView > section > div > div.pagination-container > div > span.el-pagination__sizes > div > div > input"]
type_records_child = [By.CLASS_NAME, "el-select-dropdown__item"]
type_records_li = [By.XPATH, "li"]
type_pagination = [By.CLASS_NAME, "el-pagination"]
type_pagination_li = [By.XPATH, "li"]
type_prev = [By.CLASS_NAME, "btn-prev"]
type_next = [By.CLASS_NAME, "btn-next"]
type_pagination_current = [By.CSS_SELECTOR, ".number.active"]
type_pagination_editor = [By.CSS_SELECTOR, ".el-pagination__editor > input"]
