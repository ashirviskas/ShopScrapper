import extractproduct
import extractproducts


#a = extractproduct.Shop()

#a.extract_product_info('http://www.skytech.lt/cm8066201927004-intel-core-i36300t-dual-core-330ghz-4mb-lga1151-14mm-35w-vga-tra-p-276520.html')

a= extractproducts.Shopv('http://www.skytech.lt/vaizdo-plokstes-priedai-vaizdo-plokstes-vga-c-86_85_197_284.html?sand=&pav=&sort=&grp=')

for i in  a.extract_all_products():
    print(i.name +" " +i.price)

