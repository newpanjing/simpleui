simpleui Quick Start Guide
-----
Many people will misunderstand **simpleui**. They think after downloading and installing **simpleui**, they can be used directly after startup. But **simpleui** is majorization on the basis of the **Django**. So, please [Create a Django project](#Create%2da%2dDjango%2dProject) using the command line or IDE, then [Modify the default template for simpleui](#Modify%2ddefault%2dtemplate%2dfor%2dsimpleui).

Before starting，please take a minte to understand **settings.py**, because it's especially important in the next process.

# Start Guide
  + [Create a Django project](#Create%2da%2dDjango%2dProject)
  + [Modify default template for simpleui](#Modify%2ddefault%2dtemplate%2dfor%2dsimpleui)
  + [Clone static file to the root](#Clone%2dstatic%2dfile%2dto%2dthe%2droot)
  + [Startup Project](#Startup%2dProject)
  + [How to download simpleui's template](#How%2dto%2ddownload%2dsimpleui's%2dtemplate)
  + [Switch Theme](#Switch%2dTheme)
  + [About Icons](#About%2dIcons)
# Advance Guide
  + [Default Theme](#Default%2dTheme)
  + [Customize Theme](#Customize%2dTheme)
  + [Modify Default Icon](#Modify%2dDefault%2dIcon)
  + [Modify Default Home](#Modify%2dDefault%2dHome)
  + [Modify Home Jump Address](#Modify%2dHome%2dJump%2dAddress)
  + [Modify LOGO](#Modify%2dLOGO)
  + [Configure Home Module](#Configure%2dHome%2dModule)
    + [Server Information](#Server%2dInformation)
    + [Quick Operation](#Quick%2dOperation)
    + [Recent Action](#Recent%2dAction)
  + [Use Analysis](#Use%2dAnalysis)
  + [Menu](#Menu)
    + [Customize Munu](#Customize%2dMunu)
    + [Default Icon](#Default%2dIcon)
    + [Customize Icon](#Customize%2dIcon)

  + [Modify Templates](#Modify%2dTemplates)
  + [Develop and Debug](#Develop%2dand%2dDebug)
  + [Source Code install to local](#Source%2dCode%2dinstall%2dto%2dlocal)
  + [ReWrite Page](#ReWrite%2dPage)
  + [Custom code to Header](#Custom%2dcode%2dto%2dHeader)
  + [Custom code to Footer](#Custom%2dcode%2dto%2dFooter)
  + [Custom Action](#Custom%2dAction)
  + [Offline](#Offline)
  + [Close Loading](#Close%2dLoading)
  + [admindoc](#admindoc)
# Common Problems
  + [settings.py](#Not%2dfound%2dsettings.py)
  + [python version problem](#python%2dversion%2dproblem)
  + [Unable to Start](#Unable%2dto%2dStart)
  + [Style Normal Loading But Display Abnormal](#Style%2dNormal%2dLoading%2dBut%2dDisplay%2dAbnormal)

---

## Create a Django Project

Django Documentation：[https://docs.djangoproject.com/en/2.2/intro/tutorial01/](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

## Modify default template for simpleui  

  We only need to add a line of **simpleui** in the **settings.py** of the project.

  For example 🌰：
  ```python
    # Application definition

    INSTALLED_APPS = [
        'simpleui',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
    ]
  ```
  If **DEBUG = False**, static resources will be inaccessible，please go to [Clone static file to the root](#Clone%2dstatic%2dfile%2dto%2dthe%2droot)

## Clone static file to the root
Django have a mode is **DEBUG**, it's in **settings.py**. Default **DEBUG = True**.
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```
If **DEBUG = Fasle**, there are two ways to solve the situation that static resources can't be accessed.
1. Modify **settings.py** , add following content:
```python
 STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
 ]
```
2. Clone static resources to the static directory of the project，then processed by **nginx**.
```shell
    python3 manage.py collectstatic
```
If the clone error message indicates that the static directory could't be found，please open the **settings.py** and assign a static directory
```python
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

## Startup Project
After successfully adding **simpleui** in **settings.py**，Run command：
```shell
    python manage.py runserver 8000
```
Open browser, input：http://127.0.0.1:8000/admin
if you find that the login page is different from before，Congratulations! You have successfully installed **simpleui**！Let's start enjoying **simpleui**!

## How to download simpleui's template
Currently unable to download templates，but we plan to launch **simple-admin's** html templates，can make more languages available.

## Switch Theme
Currently **simpleui** has 28 popular style themes. We will update more topics as the version is updated.

## About Icons
The icon displayed in **simpleui** can refer to the [fontawesome](https://fontawesome.com/icons?d=gallery) icon，just fill in the full class name.

## Default Theme

The default theme is configured in settings.py

```python
# Specify simpleui's default theme, specify a filename, and the relative path is read from simpleui's theme directory
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'
```

### Theme List：

> Take the corresponding file can be set as the default theme

```javascript
var SimpleuiThemes = [
    {
        text: "Default",
        menu: 'rgb(48, 65, 86)',
        logo: 'rgb(48, 65, 86)',
        top: '#FFF'
    },
    {
        text: "Simpleui-x",
        menu: '#2c2e39',
        logo: '#2c2e39',
        top: '#FFF',
        file: "simpleui.css"
    },
    {
        text: "Element-UI",
        file: "element.css",
        top: '#447eff',
        menu: '#FFf',
        logo: '#FFF'
    },
    {
        text: "layui",
        file: "layui.css",
        menu: '#393D49',
        logo: '#23262E',
        top: '#23262E'
    }, {
        text: "Ant Design Pro",
        file: "ant.design.css",
        menu: '#000b16',
        logo: '#002140',
        top: '#FFF'
    }, {
        text: "Admin LTE",
        file: "admin.lte.css",
        top: '#3c8dbc',
        logo: '#3c8dbc',
        menu: '#2b3539'
    }, {
        text: "Highdmin",
        file: "highdmin.css",
        top: '#02c0ce',
        menu: '#e0e0e0',
        logo: '#02c0ce'
    }, {
        text: "Aircraft",
        file: "aircraft.css",
        top: '-webkit-gradient(linear, left bottom, left top, color-stop(0, #4d5b76), color-stop(1, #6f80a1)) !important',
        menu: '#e0e0e0',
        logo: '-webkit-gradient(linear, left bottom, left top, color-stop(0, #4d5b76), color-stop(1, #6f80a1)) !important'
    }, {
        text: "Purple",
        file: "purple.css",
        top: '#FFF',
        logo: '#FFF',
        menu: '#3e4295'
    }, {
        text: "Gray",
        file: "gray.css",
        top: '#213a53',
        logo: '#213a53',
        menu: '#e0e0e0'
    },
    {
        text: "Dark green",
        file: "dark.green.css",
        top: '#f3f3f4',
        menu: '#283846',
        logo: '#283846'
    },
    {
        text: "Orange",
        file: "orange.css",
        top: 'linear-gradient(to right bottom, #da8342, #e45131)',
        logo: 'linear-gradient(to right bottom, #da8342, #e45131)',
        menu: '#FFF'
    },
    {
        text: "Black",
        file: "black.css",
        top: "#333",
        logo: "#333",
        menu: '#FFF'
    },
    {
        text: "Green",
        file: "green.css",
        top: '#19a97b',
        logo: '#FFF',
        menu: '#FFF'
    },
    {
        text: "Light",
        file: "light.css",
        top: "#ebf1f5",
        logo: "#ebf1f5",
        menu: "#ebf1f5"
    }, {
        text: 'Enterprise blue',
        file: 'e-blue.css',
        top: '#3ba1df',
        logo: '#3ba1df',
        menu: '#FFF'
    }, {
        text: 'Enterprise blue pro',
        file: 'e-blue-pro.css',
        top: '#3ba1df',
        logo: '#3ba1df',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise green',
        file: 'e-green.css',
        top: '#27ad60',
        logo: '#27ad60',
        menu: '#FFF'
    }, {
        text: 'Enterprise green pro',
        file: 'e-green-pro.css',
        top: '#27ad60',
        logo: '#27ad60',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise red',
        file: 'e-red.css',
        top: '#c9333e',
        logo: '#c9333e',
        menu: '#FFF'
    }, {
        text: 'Enterprise red pro',
        file: 'e-red-pro.css',
        top: '#c9333e',
        logo: '#c9333e',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise purple',
        file: 'e-purple.css',
        top: '#8263b1',
        logo: '#8263b1',
        menu: '#FFF'
    }, {
        text: 'Enterprise purple pro',
        file: 'e-purple-pro.css',
        top: '#8263b1',
        logo: '#8263b1',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise black',
        file: 'e-black.css',
        top: '#1f2c39',
        logo: '#1f2c39',
        menu: '#FFF'
    }, {
        text: 'Enterprise black pro',
        file: 'e-black-pro.css',
        top: '#1f2c39',
        logo: '#1f2c39',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-green',
        file: 'x-green.css',
        top: '#2F9688',
        logo: '#2F9688',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-red',
        file: 'x-red.css',
        top: '#AA3130',
        logo: 'rgb(38, 50, 56)',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-blue',
        file: 'x-blue.css',
        top: '#FFF',
        logo: '#1E9FFF',
        menu: 'rgb(38, 50, 56)'
    }
]
```

## Customize Theme
Before customizing the theme, please clone the static resources of **simpleui** to the root directory. Then you need to find **theme.js**, it's used to configure the list of topics.

Please configure in this format.

```javascript
var SimpleuiThemes = [
    {
        "text": "Default"
    },
    {
        "text": "Simpleui-x",
        "file": "simpleui.css"
    },
    .....
]
```

Before adding your style, please understand how **less** to used.

Example for **admin.lte.less**
```css
@import "base";

@primary: #2096c8 !important;
@color: white;

@menu-color: #8aa4af !important;
@menu-background: #2b3539 !important;

@menu-color-hover: #FFF;
@menu-background-hover: #1f272b;

@menu-title-color: #FFF;
@menu-title-background-color: #212c32;

@menu-title-color-hover: #FFF;
@menu-title-background-color-hover: #1f272b;


@navbar-color: #fff;
@navbar-background: #3c8dbc;
```
It will compile to **admin.lte.css**. 
You need to install **less**.
```shell
npm install less -g

lessc admin.lte.less>admin.lte.css
```

## Modify Default Icon
Django's built-in authentication and authorization and associated users and groups have been configured with an icon by default. Custom app will be the default icons and need to be configured in the **settings.py** file.

## Modify Default Home
**simpleui** has a default home page, which consists of quick navigation and recent operations.

You can modify the default home page and add it to your project's **settings.py**：

+ Home configuration
> SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
+ Home title
> SIMPLEUI_HOME_TITLE = 'My Home Title'
+ Home Icon,support `element-ui's` and `fontawesome's` icon，reference https://fontawesome.com/icons
> SIMPLEUI_HOME_ICON = 'fa fa-user'

The above three configurations are optional. If you don't fill, there will be default values. [Icon List](https://fontawesome.com/icons)

## Modify Home Jump Address
The top of the home page has a default jump address of /, this is root directory. If you need to customize, add some settings in your project's **settings.py**.

```python
# Configure simpleui Click the address of the home icon to jump.
SIMPLEUI_INDEX = 'https://www.88cto.com'
```

Relative and absolute paths can be set. There is nothing special about this address, it will call **window.open** to open the address directly.


## Modify LOGO
+ Customize SIMPLEUI's Logo
> SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

## Config Home Module
The home page displays three modules by default, server information, quick operation and recent actions. You can show or hide some modules as needed.
### Server Information
Hide：
> SIMPLEUI_HOME_INFO = False

Display：
> SIMPLEUI_HOME_INFO = True

### Quick Operation

Hide：
> SIMPLEUI_HOME_QUICK = False

Display：
> SIMPLEUI_HOME_QUICK = True

### Recent Action

Hide：
> SIMPLEUI_HOME_ACTION = False

Display：
> SIMPLEUI_HOME_ACTION = True

## Use Analysis
`Default is True, statistical analysis information is only used to better help simpleui improvements, and doesn't read sensitive information. And the analysis data will not be shared with any third party.`
> SIMPLEUI_ANALYSIS = False

|Values|Description|
|--|--|
|True|Collect and analyze,report only one analysis data a day。Default is True|
|False|Don't collect and analyze|

## Menu

### Customize Munu

#### Keep system menu
system_keep field is used to tell **simpleui**，whether you need to keep the system default menu, the default is False, don't keep.
If changed to True，custom and system menus will coexist.

#### Menus Description

|Values|Description|
|---|---|
|name|Menu name|
|icon|Icon，refer element-ui和fontawesome|
|url|link address，absolute or relative, if there is a models field, the url will be ignored|
|models|submenu, Since 2021.02.01+ version supports up to 3 levels of menus|
|newTab|boolean,default:False,Open it in a browser TAB|

#### Example
```python
SIMPLEUI_CONFIG = {
    'system_keep':False,
    'menus': [{
        'name': 'Simpleui',
        'icon': 'fas fa-code',
        'url': 'https://gitee.com/tompeppa/simpleui'
    }, {
        'app': 'auth',
        'name': 'Permission',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': 'users',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }, {
      	# Since 2021.02.01+ supports multi-level menus, models is the submenu name
        'name': 'Multi-level menu test',
        'icon': 'fa fa-file',
        'models': [
          {
            'name': 'IQiyi',
            # The fourth level is not supported, the element only supports level 3
            'models': [
              {
                'name': 'Movie',
                'url': 'https://www.iqiyi.com/dianying/',
                'newTab': True
              }, {
                'name': 'TV series',
                'url': 'https://www.iqiyi.com/dianshiju/'
              },
            ]
          }, {
            'name': 'Network',
            'url': 'https://www.wezoz.com',
            'icon': 'fab fa-github'
        }]
    }]
}
```

If there is a **menus** field in **SIMPLEUI_CONFIG**，will override the system default menu。And the **menus** output in menus are not controlled by permissions。

### Default Icon
**simpleui** provides a default file icon for all menus for uniform style. Maybe you don't like it, you can choose to turn off the default icon.

>SIMPLEUI_DEFAULT_ICON = False

|Values|Description|
|--|--|
|True|Turn on the default icon，default is True|
|False|Turn off the default icon|

### Customize Icon
**simpleui** only provides icons for the system default module. If you want to specify icons for other modules, you can customize the configuration. Icon reference please refer to：[About Icons](#About%2dIcons)

Priority：
Custom Icon->System Icon->Default Icon

>Note：**simpleui** doesn't involve code in principle, so use the **setting** method. In the future, may be consider extending the **Model**'s **Meta class** for configuration icons.

|Values|Description|
|---|---|
|name|Module name, please note it's not the name of the **model**, it's the text displayd on the menu, because the **model** can be repeated, it will lead to indistinguishable|
|icon|Icon name|
For example：
```
SIMPLEUI_ICON = {
    'System_Manage': 'fab fa-apple',
    'Employeee_Manage': 'fas fa-user-tie'
}

```

## Modify Templates
Modify the template based on **simpleui** need to require some understanding of django
1. Clone **simpleui** into a static directory，refer to [Clone static file to the root](#Clone%2dstatic%2dfile%2dto%2dthe%2droot)
2. Find the admin directory in the static directory,inner is the template of **simpleui**, directly modify the relevant html page to take effect.

## Develop and Debug
If you want to make some modifications based on **simpleui**, you can refer to the following steps:
1. Install **simpleui** into the project
2. Find the directory of **simpleui** and delete
3. Clone **simpleui** source to local
4. In the Linux、Unix、macOS environments，use the flexible connection method to assign the **simpleui** directory in the project dependency package to the **simpleui** directory of the source code.
    ```shell
    ln -s sourceFile TargetFile
    ```
5. Right clicl on the windows environment to create a shortcut.

Then you can modify and publish **simpleui**. If you have any questions, please join the QQ group：786576510
## Source Code install to local
+ Clone source code local installation
```shell
git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```
Next steps please refer to [Modify default template for simpleui](#Modify%2ddefault%2dtemplate%2dfor%2dsimpleui)

## ReWrite Page

For example, rewrite the home page, create a new **admin** folder in the **templates** directory, and then add a index.html
If you choose **extends**, you can only use **block**  
for example：
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {%block head}
        {{ block.super }}
        ..your code..
    {% endblock %}

    {% block script %}
        {{ block.super }}
        ..your code..
    {% endblock %}
```

If you want to rewrite all：

```html
<html>
    <head>
        <title>Custom Code</title>
    </head>
    <body>
        your code
    </body>
</html>
```
##  Custom code to Header
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {%block head}
        {{ block.super }}
        ..your code..
    {% endblock %}
```
##  Custom code to Footer
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {% block script %}
        {{ block.super }}
        ..your code..
    {% endblock %}
```

## Custom Action
> Must be version 2.1.2 or above

Django admin provides support for custom buttons by default, but styles and ICONS are not customizable. Simpleui adds custom styles, ICONS and button types to django admin custom action.

Code：
```python
@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'idCard', 'phone', 'birthday', 'department', 'enable', 'create_time')
   
    # add action
    actions = ['make_copy', 'custom_button']

    def custom_button(self, request, queryset):
        pass

    # display text，Consistent with django admin
    custom_button.short_description = 'Test Button'
    # icon，reference：element-ui icon and https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # Specify button type：https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # Custom style
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass
    make_copy.short_description = 'Copy employe'
```

Configuration compatible with native admin
### Field:

|Field|Description|
|------|------|
|icon|Button icon，Reference：https://element.eleme.cn/#/zh-CN/component/icon and https://fontawesome.com，copy class|
|type|Button type，Reference：https://element.eleme.cn/#/zh-CN/component/button|
|style|Customize CSS styles|
|confirm|Requires version 3.4 or above|

+ confirm demo

```python
    def message_test(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, 'Success')
        
    # Add confirmation to button
    message_test.confirm = 'Are you sure?'
```


+ Link Button

> Requires version 2.9 or above

|Field|Description|
|------|------|
|action_type|0=The current page, 1=Simpleui New tab，2=Browser new tab|
|action_url|The url address|



### layer dialog button

> Effective in 2021.1.0 and above

The dialog button is to configure the action in the admin, you can customize the input fields, and then through the ajax request to the action for business processing.

Need to inherit `AjaxAdmin` in `from simpleui.admin import AjaxAdmin` package

`simplepro` will also support the dialog button function synchronously.

#### Effect
<img src="/images/layer.png" alt="layer">

#### Field Description

The following fields refer to the `layer` property of `action`

|Field|Description|
|--|--|
|title|Dialog title|
|tips|Dialog prompts|
|confirm_button|Confirm button text|
|cancel_button|Cancel button text|
|width|The width of the dialog box, in percentage, for example: 50%|
|labelWidth|The label width of the table, for example: 80px|
|params|Fields in the dialog table, array|

##### params field

|Field|Description|
|--|--|
|type|Type, value: input native attributes, and elementui: select, date, datetime, rate, color, slider, switch, input_number, checkbox, radio|
|key|Parameter name, the name obtained in the post parameter|
|value|default value, array or text|
|label|The name of the field displayed in the table|
|size|The size of the component, the value is: medium / small / mini|
|require|is required, the value is: True/False|
|width|The width of the input box, for example: 200px|
|options|options, array, available when type is select, checkbox, radio|

#### options field
|Field|Description|
|--|--|
|key|value|
|label|Display text|


#### Examples

```python
class RecordAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    resource_class = ProxyResource

    list_display = ('id','name','type','money','create_date')
    list_per_page = 10

    actions = ('layer_input',)

    def layer_input(self, request, queryset):
        # The queryset here will filter data and only include the selected data

        post = request.POST
        # After getting the data here, you can do some business processing
        # _action in post is the method name
        # post _selected is the selected data, separated by commas
        if not post.get('_selected'):
            return JsonResponse(data={
                'status':'error',
                'msg':'Please select the data first! '
            })
        else:
            return JsonResponse(data={
                'status':'success',
                'msg':'Processed successfully! '
            })

    layer_input.short_description ='Pop up dialog box input'
    layer_input.type ='success'
    layer_input.icon ='el-icon-s-promotion'

    # Specify an input parameter, which should be an array

    # Designated as a pop-up layer, this parameter is the most critical
    layer_input.layer = {
        # Input box configuration in the pop-up layer

        # Specify the title of the dialog box here
        'title':'Pop-up layer input box',
        # Tips
        'tips':'This pop-up dialog box needs to be defined in the admin, and the new data editing and other functions need to be implemented by yourself. ',
        # Confirm button display text
        'confirm_button':'Confirm submission',
        # Cancel button display text
        'cancel_button':'Cancel',

        # The width of the pop-up layer dialog, the default is 50%
        'width': '40%',

        # The width of the label in the form, corresponding to the label-width of element-ui, the default is 80px
        'labelWidth': "80px",
        'params': [{
            # The type here corresponds to the native input attribute of el-input, the default is input
            'type':'input',
            # key corresponds to the key in the post parameter
            'key':'name',
            # Displayed text
            'label':'Name',
            # Is empty check, the default is False
            'require': True
        }, {
            'type':'select',
            'key':'type',
            'label':'Type',
            'width': '200px',
            # size corresponds to the size of elementui, the value is: medium / small / mini
            'size':'small',
            # The value field can specify the default value
            'value': '0',
            'options': [{
                'key': '0',
                'label':'Income'
            }, {
                'key': '1',
                'label':'Expenses'
            }]
        }, {
            'type':'number',
            'key':'money',
            'label':'Amount',
            # Set default value
            'value': 1000
        }, {
            'type':'date',
            'key':'date',
            'label':'Date',
        }, {
            'type':'datetime',
            'key':'datetime',
            'label':'Time',
        }, {
            'type':'rate',
            'key':'star',
            'label':'evaluation level'
        }, {
            'type':'color',
            'key':'color',
            'label':'color'
        }, {
            'type':'slider',
            'key':'slider',
            'label':'slider'
        }, {
            'type':'switch',
            'key':'switch',
            'label':'switch switch'
        }, {
            'type':'input_number',
            'key':'input_number',
            'label':'input number'
        }, {
            'type':'checkbox',
            'key':'checkbox',
            # Must specify default value
            'value': [],
            'label':'Checkbox',
            'options': [{
                'key': '0',
                'label':'Income'
            }, {
                'key': '1',
                'label':'Expenses'
            }, {
                'key': '2',
                'label':'Profit'
            }]
        }, {
            'type':'radio',
            'key':'radio',
            'label':'Single selection box',
            'options': [{
                'key': '0',
                'label':'Income'
            }, {
                'key': '1',
                'label':'Expenses'
            }, {
                'key': '2',
                'label':'Profit'
            }]
        }]
    }


```

#### action returns results

```json
{
    'status':'error',
    'msg':'Please select the data first! '
}
```

> status = success/error

> msg = custom

#### Dialog button description

1. If you need to add and edit, you need to implement the business logic yourself, just fill the value field with the data when editing.

2. Data can only be submitted after the restriction is selected, and can be restricted in the background

3. Versions 2020.1.0 and above take effect, you need to inherit `AjaxAdmin` in the `from simpleui.admin import AjaxAdmin` package. 500 or 404 if not inherited submitted data
E.g:

```python

 if not post.get('_selected'):
            return JsonResponse(data={
                'status':'error',
                'msg':'Please select the data first! '
            })

```

### Layer file upload

>starting with version 2021.4.2+, supports uploading files in Layer

Example:

```python

@admin.register(Layer)
class LayerAdmin(AjaxAdmin):
actions = ('upload_file',)

def upload_file(self, request, queryset):
# Upload is the same key as the key used in params
upload= request.FILES['upload']
print(upload)
pass

Upload_file.short_description = 'File Upload Dialog'
upload_file.type = 'success'
upload_file.icon = 'el-icon-upload'
upload_file.enable = True

upload_file.layer = {
'params': [{
'type': 'file',
'key': 'upload',
'label': 'file'
}]
}

` ` `

## Offline

> Requires version 2.1.3 or above

settings.py:
```python
SIMPLEUI_STATIC_OFFLINE = True
```
Specifies whether simpleui loads static resources in offline mode. When true, all resources will be read locally by default, even if there is no networking. Suitable for intranet projects

If you do not fill in the item or are false, the default is obtained from the third-party CDN.

## Close Loading

> Requires version 2.1.5 or above

settings.py:
```python
SIMPLEUI_LOADING = False
```

## admindoc
Admindoc must be the simpleui3.3+ version

## Common Problems
  ### Not found settings.py

    The file is in the django project, not in simpleui. If you are familiar with django, you will understand, if you are not familiar, please learn django first.[django documentation](https://docs.djangoproject.com/en/2.2/)

  ### python version problem

    + this project is recommended to use python3.x, python2.x may not be compatible.
    + If you make a mistake when using source installation, please specify the python version, python3 and pip3
  ### Unable to Start
  May be unable to start due to some unknown problem, please don't give up **simpleui**, you can commit [issue](https://github.com/newpanjing/simpleui/issues)，or join QQ group directly：786576510，we will assist in solving.

  ### Style Normal Loading But Display Abnormal
  in the **Windows8** system, you may encounter that **css** and other files are all loaded normally, but the display is not normal.this is because the response header is **application/x-css**, not **text/css**, causing the browser to not parse properly.
  #### Solution：
1.Run cmd： Input **regedit** and click Enter
    
2.Find the **.css** in the registry **HKEY_CLASSES_ROOT** click on the **.css** floder Modify the **Content Type** to **text/css**.

Reference：[https://blog.csdn.net/sun754276603/article/details/46989965](https://blog.csdn.net/sun754276603/article/details/46989965)

>For more questions, please commit [issues](https://github.com/newpanjing/simpleui/issues) to us.