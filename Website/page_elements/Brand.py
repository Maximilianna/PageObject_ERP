from selenium.webdriver.common.by import By


type_brand = [By.LINK_TEXT, "商品品牌"]
type_new_brand = [By.CLASS_NAME, "el-icon-plus"]
type_add_brand_name = [By.CSS_SELECTOR, ".el-col.el-col-16 > .el-input.el-input--medium > input"]
type_save_button = [By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--medium > span"]
type_cancel_button = [By.CSS_SELECTOR, ".el-button.el-button--default.el-button--medium > span"]
type_query_brand_name = [By.CSS_SELECTOR, ".el-form-item__content >.el-input > .el-input__inner"]
type_query_brand_status = [By.CSS_SELECTOR, ".el-form-item__content > .el-select >.el-input > .el-input__inner"]
type_query_brand_ul = [By.CLASS_NAME, "el-select-dropdown__item"]
type_query_brand = [By.XPATH, "//i[@class=\"el-icon-search\"]/.."]
type_records = [By.CSS_SELECTOR, ".el-input.el-input--mini.el-input--suffix > .el-input__inner"]
type_records_ul = [By.CLASS_NAME, "el-select-dropdown__item"]
type_pagination_current = [By.CSS_SELECTOR, ".number.active"]
type_pagination_entirety = [By.CSS_SELECTOR, ".number"]
type_quick_next = [By.CLASS_NAME, "btn-quicknext"]
type_quick_prev = [By.CLASS_NAME, "btn-quickprev"]
