# Georgia Tech Master Data File Package Overview  

## Included Files
- IceCat_Cat_2833_feather.zip
- IceCat Specifications/CategoriesList.xml
- IceCat Specifications/CategoryFeaturesList.xml

## Data
The full IceCat dataset provided can be found within the *IceCat_Cat_2833_feather.zip* file. The ZIP file contains 495
*.feather* files. Each one represents a full corpus of products under a specific category. All products come from the
large sub-root category *Computers & Peripherals* from [IceCat](https://icecat.co.uk/en/search/computers-peripherals) (
Note that since products are added on a continuous basis , the provided dataset does not represent the current full 
corpus of IceCat. Nor does it include those products that are marked as proprietary by IceCat and excluded from the 
public dataset)

All files are in a *.feather* file format and can be easily read [with Python](https://arrow.apache.org/docs/python/feather.html).

Each category dataset contains 4 constant attributes:
- id -> The unique identifier of the product.
- name -> The name of the product.
- category_id -> The unique category ID the product is categorized under.
- category_label -> The category name the product is categorized under.

The remaining attributes are category specific. Where each attributes come in two parts. First is the attribute value 
and right after the attribute's unit value. Ex:

| ... | Temperature.3646 |  Temperature.3646.unit | ... |
|-----|-----------------:|-----------------------:|-----|
| ... |              100 |                     °C | ... |

The number within the attribute name represents the unique IceCat Attribute ID for that attribute which can be used for
cross-reference within the *IceCat Specifications/CategoryFeaturesList.xml* file.

## Category Hierarchy
The *IceCat Specifications/CategoriesList.xml* file provides an overview of the category hierarchy within IceCat. The
file contains multiple `<Category>` elements Each one providing a description of the category and pointing to its parent,
except for category with `ID="1"` which is the root of the entire category tree.

```xml
<CategoriesList>
    <Category ID="2"> -> The category ID
        <Versions>
            <UNSPSC code="43230000" version="20.0601" date_added="2019-02-07 09:26:48" Updated="2021-01-19 13:27:57" />
        </Versions>
        <Description ID="548795" Value="Instructions for a computer's processor to perform specific operations e.g. system software such as Windows and iOS, application software such as internet browsers and apps." /> -> Category Description
        <Keywords ID="331" Value="" langid="1" Updated="2021-01-19 13:27:57" />
        <Name ID="3727364" Value="Software" langid="1" Updated="2018-02-14 15:44:49" /> 
        <ParentCategory ID="2833"> -> The parent of this category denoted by the "ID" attribute of the element which corresponds to another <Category/> element
            <Names>
                <Name ID="3729373" Value="Computers &amp; Peripherals" langid="1" Updated="2020-05-14 16:39:06" />
                </Names>
        </ParentCategory>
    </Category>
    ...
    <Category ID="2833"> -> The parent ID from above corresponds to this Category ID.
        <Versions>
            <UNSPSC code="52000000" version="20.0601" date_added="2019-02-07 09:27:05" Updated="2021-01-19 13:27:57" />
        </Versions>
        <Keywords ID="78800" Value="" langid="1" Updated="2021-01-19 13:27:57" />
        <Name ID="3729373" Value="Computers &amp; Peripherals" langid="1" Updated="2020-05-14 16:39:06" />
        <ParentCategory ID="1">
            <Names />
        </ParentCategory>
    </Category>
</CategoriesList>
```

## Attribute to Category Mapping.

Each category has assigned to it a predefined list of attributes (within IceCat 
the term used is `Feature`). This mapping can be found within the *IceCat Specifications/CategoryFeaturesList.xml* file. 
Similarly to the *CategoriesList.xml*, the file contains a number of `<Category>` elements each containing a list of 
features. The `<Category>` element has an attribute `ID` which corresponds to the `ID` within th *CategoriesList.xml*. 
The `Feature` elements each contains the name of the attribute and the corresponding unit. Some features have a restriction
on the values that can be added to them which is explicitly stated through the use of the `<RestrictedValue>` element, 
listing all the permitted values. As mentioned in [Data](#data) the values of the `ID` attributes of the `<Feature>` 
elements are preserved within the *.feather* files so that they can be cross-referenced here if needed.

```xml
<CategoryFeaturesList Code="1">
    <Category ID="2" LowPic="http://images.icecat.biz/img/low_pic/2-8879.jpg" UNCATID="43160000" Updated="2020-12-17 11:29:58">
        <CategoryFeatureGroup ID="120" No="0">
            <FeatureGroup ID="0">
                <Name ID="5073" Value="Technical details" langid="1" Updated="2020-12-15 14:27:37" />
            </FeatureGroup>
        </CategoryFeatureGroup>
        <Feature CategoryFeatureGroup_ID="120" CategoryFeature_ID="111" Class="0" ID="66" LimitDirection="0" Mandatory="0" No="111226" Searchable="0" Type="numerical" Use_Dropdown_Input="N" ValueSorting="0" Updated="1970-01-01 23:00:00">
            <Measure ID="19" Sign="MB" Updated="2008-03-09 17:19:09">
                <Sign>MB</Sign>
                <Signs>
                    <Sign ID="15506" langid="1" Updated="2013-12-03 10:19:26">MB</Sign>
                </Signs>
            </Measure>
            <Name ID="1469" Value="Minimum storage drive space" langid="1" Updated="2018-12-27 16:41:27" />
            <RestrictedValue />
        </Feature>
        <Feature CategoryFeatureGroup_ID="120" CategoryFeature_ID="112" Class="0" ID="68" LimitDirection="0" Mandatory="0" No="111225" Searchable="0" Type="numerical" Use_Dropdown_Input="N" ValueSorting="0" Updated="1970-01-01 23:00:00">
            <Measure ID="19" Sign="MB" Updated="2008-03-09 17:19:09">
                <Sign>MB</Sign>
                <Signs>
                    <Sign ID="15506" langid="1" Updated="2013-12-03 10:19:26">MB</Sign>
                </Signs>
            </Measure>
            <Name ID="1473" Value="Minimum RAM" langid="1" Updated="2020-12-15 14:27:37" />
            <RestrictedValue />
        </Feature>
        <Feature CategoryFeatureGroup_ID="120" CategoryFeature_ID="147082" Class="0" ID="18767" LimitDirection="0" Mandatory="0" No="100000" Searchable="0" Type="dropdown" Use_Dropdown_Input="N" ValueSorting="1" Updated="2016-02-09 08:17:15">
            <Measure ID="29" Sign="" Updated="2006-02-07 19:03:11">
                <Sign />
                <Signs />
            </Measure>
            <Name ID="1416129" Value="Processor codename" langid="1" Updated="2014-12-22 12:57:40" />
            <RestrictedValue>Broadwell</RestrictedValue>
            <RestrictedValue>Haswell</RestrictedValue>
            <RestrictedValue>Ivy Bridge</RestrictedValue>
            <RestrictedValue>Sandy Bridge</RestrictedValue>
            <RestrictedValue>Bay Trail</RestrictedValue>
            <RestrictedValue>Crystal Well</RestrictedValue>
            <RestrictedValue>Mendocino</RestrictedValue>
            <RestrictedValue>Yonah</RestrictedValue>
        </Feature>
    </Category>
</CategoryFeaturesList>
```