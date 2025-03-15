import { Product } from '../../types';
import { applyCategories } from '../applyCategories';

const afterFilterProducts =  [{
    id: 1,
    name: "name",
    description: "description",
    price: 100,
    priceSymbol: '₽',
    category: "Электроника",
}]
const products = [{id: 1,
    name: "name",
    description: "description",
    price: 100,
    priceSymbol: '₽',
    category: "Электроника",},
    {id: 1,
        name: "name",
        description: "description",
        price: 100,
        priceSymbol: '₽',
        category: "Одежда",}]

describe('test applyCategories', () => {
    it('must filter list', () => {
        expect(applyCategories(products as Product[], ["Электроника"])
        ).toStrictEqual(afterFilterProducts);
    });

    it('should return empty', () => {
        expect(applyCategories([], ["Электроника"])
        ).toStrictEqual([]);
    });
});
