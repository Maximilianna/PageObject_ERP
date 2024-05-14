文件关系树
```
PageObject_ERP
├─ Driver
│  └─ driver.py
├─ Website
│  ├─ model
│  │  ├─ function.py
│  │  └─ myunit.py
│  ├─ page_elements
│  │  ├─ Base.py
│  │  ├─ Brand.py
│  │  ├─ Login.py
│  │  └─ Manage.py
│  ├─ page_objects
│  │  ├─ BasePage.py
│  │  ├─ BrandPage.py
│  │  ├─ LabelsPage.py
│  │  ├─ LoginPage.py
│  │  ├─ ManagePage.py
│  │  └─ MessagePage.py
│  ├─ test_cases
│  │  ├─ add_Brand_Test.py
│  │  └─ add_Commodity_Test.py
│  ├─ test_datas
│  │  └─ add_Commodity_Test.csv
│  ├─ test_report
│  └─ run_test.py
└─ README.md
```

页面对象继承关系树

```
BasePage
├─ LabelsPage
│  └─ ManageDataPage
│    ├─ ManagePage
│    └─ BrandPage
└─ LoginPage
```

