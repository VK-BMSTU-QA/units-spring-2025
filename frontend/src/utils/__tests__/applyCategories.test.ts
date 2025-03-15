import { Product } from '../../types';
import { applyCategories } from '../applyCategories';


const products = [
    { id: 1, description: 'Рубашка', category: 'Одежда', price: 1, name: 'name' } as Product,
    { id: 2, description: 'Самовар', category: 'Для дома', price: 100, name: 'second name' } as Product,
    { id: 3, description: 'Комп', category: 'Электроника', price: 100, name: 'third name' } as Product
]

describe('test update categories function', () => {
    it('should return product by categories', () => {
        expect(applyCategories([products[0], products[1]], ['Одежда'])).
            toStrictEqual([products[0]])

        expect(applyCategories([products[0], products[1]], ['Одежда', 'Электроника'])).
            toStrictEqual([products[0]])

        expect(applyCategories(products, [])).
            toStrictEqual(products)

        expect(applyCategories(products, ['Электроника', 'Одежда', 'Для дома'])).
            toStrictEqual(products)

    });
});