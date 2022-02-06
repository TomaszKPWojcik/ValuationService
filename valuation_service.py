from product import Product
from io_manager import IoManager

fpc = r'cvs_files\currencies.csv'
fpd = r'cvs_files\data.csv'
fpm = r'cvs_files\matchings.csv'
fpo = r'cvs_files\top_products.csv'

if __name__ == '__main__':
    currencies_reader = IoManager(fpc)
    currencies_reader.read()
    currenciesdict = currencies_reader.getDict()

    matchings_reader = IoManager(fpm)
    matchings_reader.read()
    matchingsdict = matchings_reader.getDict()

    data_reader = IoManager(fpd)
    data_reader.read()

    product_list = []
    for line in data_reader.lines:
        l = line.strip().split(',')
        if len(l) == 5:
            product_list.append(Product(l[0], l[1], l[2], l[3], l[4], currenciesdict))

    #group by matching_id
    product_group = {}
    for p in product_list:
        if p.matching_id in product_group.keys():
            pl = product_group[p.matching_id]
            pl.append(p)
        else:
            product_group[p.matching_id] = [p]

    output_lines = ['matching_id,total_price,avg_price,currency,ignored_products_count\n']
    for i in product_group:
        htp = max([p.total_price for p in product_group[i]])
        ap = sum([p.total_price for p in product_group[i]])/len(product_group[i])
        output_lines.append(f'{i},{htp},{ap},{product_group[i][0].currency},0\n')

    top_product_writer = IoManager(fpo)
    top_product_writer.write(output_lines)
