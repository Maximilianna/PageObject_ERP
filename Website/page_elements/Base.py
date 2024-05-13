from selenium.webdriver.common.by import By

type_labels = [By.CLASS_NAME, "tags-view-item"]
type_label = [By.CLASS_NAME, "el-icon-close"]
type_pagination = [By.CSS_SELECTOR, ".el-pager > .number"]
type_pagination_current = [By.CSS_SELECTOR, ".number.active"]
type_pagination_entirety = [By.CSS_SELECTOR, ".number"]
type_quick_next = [By.CLASS_NAME, "btn-quicknext"]
type_quick_prev = [By.CLASS_NAME, "btn-quickprev"]
type_prev = [By.CLASS_NAME, "btn-prev"]
type_next = [By.CLASS_NAME, "btn-next"]
type_records = [By.CSS_SELECTOR, ".el-input.el-input--mini.el-input--suffix > .el-input__inner"]
type_records_li = [By.XPATH, "//li[@class=\"el-select-dropdown__item selected\"]/../li"]
