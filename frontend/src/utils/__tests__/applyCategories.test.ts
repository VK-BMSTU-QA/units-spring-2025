import { applyCategories } from '../applyCategories'
import type { Product, Category } from '../../types';

describe('test apply categories funtion', () => {

    const products = [{
        id: 0,
        name: 'lamp',
        description: '',
        price: 100,
        category: 'Электроника'
    },
    {
        id: 1,
        name: 'table',
        description: '',
        price: 200,
        category: 'Для дома'
    }
    ] as Product[];

    it('returns all products if categories is empty', () => {
        expect(applyCategories([...products], [])).toStrictEqual(products);
        expect(applyCategories([], [])).toStrictEqual([]);
    });

    it.each([
        [[...products], ['Для дома'], [products[1]]],
        [[...products], ['Электроника'], [products[0]]],
        [[...products], ['Для дома', 'Электроника'], products],
        [[...products], ['Одежда'], []]])
        ('returns all products %p in given category %p', (allProducts, categories, expected) => {
            expect(applyCategories(allProducts as Product[], categories as Category[])).toStrictEqual(expected)
        });

});
