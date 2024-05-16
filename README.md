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
│  │  ├─ Labels.py
│  │  ├─ Login.py
│  │  ├─ Manage.py
│  │  ├─ Message.py
│  │  └─ WareHouse.py
│  ├─ page_objects
│  │  ├─ BasePage.py
│  │  ├─ BrandPage.py
│  │  ├─ CategoryPage.py
│  │  ├─ CompanyPage.py
│  │  ├─ LabelsPage.py
│  │  ├─ LoginPage.py
│  │  ├─ ManagePage.py
│  │  ├─ MessagePage.py
│  │  └─ WareHousePage.py
│  ├─ test_cases
│  │  ├─ add_Brand_Test.py
│  │  ├─ add_Category_Test.py
│  │  ├─ add_Commodity_Test.py
│  │  ├─ add_Company_Test.py
│  │  └─ add_WareHouse_Test.py
│  ├─ test_datas
│  │  ├─ add_Brand_Test.csv
│  │  └─ add_Commodity_Test.csv
│  ├─ test_report
│  └─ run_test.py
├─ Wiki.md
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

具体功能请看Wiki.md