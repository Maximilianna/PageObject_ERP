from selenium.webdriver.common.by import By

type_new = [By.CLASS_NAME, "el-icon-plus"]
type_query = [By.XPATH, "//i[@class=\"el-icon-search\"]/.."]
type_reset = [By.XPATH, "//i[@class=\"el-icon-refresh\"]/.."]
type_pagination = [By.CSS_SELECTOR, ".el-pager > .number"]
type_pagination_current = [By.CSS_SELECTOR, ".number.active"]
type_pagination_entirety = [By.CSS_SELECTOR, ".number"]
type_quick_next = [By.CLASS_NAME, "btn-quicknext"]
type_quick_prev = [By.CLASS_NAME, "btn-quickprev"]
type_prev = [By.CLASS_NAME, "btn-prev"]
type_next = [By.CLASS_NAME, "btn-next"]
type_records = [By.CSS_SELECTOR, ".el-input.el-input--mini.el-input--suffix > .el-input__inner"]
type_data_modify = [By.CSS_SELECTOR, ".el-table__row:nth-child( ) > td:nth-last-child(1) > div > button:nth-child(1)"]
type_data_switch = [By.CSS_SELECTOR, ".el-table__row:nth-child( ) > td:nth-last-child(1) > div > button:nth-child(2)"]
type_save_button = [By.CSS_SELECTOR,
                    ".el-dialog__body + .el-dialog__footer > .dialog-footer > .el-button--primary > span"]
type_cancel_button = [By.CSS_SELECTOR,
                      ".el-dialog__body + .el-dialog__footer > .dialog-footer > .el-button--default > span"]
type_name = [By.CSS_SELECTOR, ".el-col-16 > .el-input > input"]
type_into_page = [By.LINK_TEXT, ""]
type_query_name = [By.CSS_SELECTOR, ".el-form-item__content >.el-input > .el-input__inner"]
type_query_status = [By.CSS_SELECTOR, ".el-form-item__content > .el-select >.el-input > .el-input__inner"]
type_li = [By.CLASS_NAME, "el-select-dropdown__item"]
