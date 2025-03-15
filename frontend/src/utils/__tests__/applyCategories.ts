import { applyCategories } from "../applyCategories"
import type { Category, Product } from '../../types';

describe('test apply categories function', () => {
    const skirt = { category: 'Одежда' } as Partial<Product>;
    const table = { category: 'Для дома' } as Partial<Product>;
    const phone = { category: 'Электроника' } as Partial<Product>;
    const products = [ skirt, table, phone ] as Product[];

    const emptyCategories: [] = [];
    const oneCategory = ['Для дома'] as Category[];
    const twoCategories = ['Одежда', 'Электроника'] as Category[];
    const allCategories = ['Для дома', 'Одежда', 'Электроника'] as Category[];

    it('should return all products if categories are empty', () => {
        expect(applyCategories(products, emptyCategories)).toEqual(products);
    });

    it('should return all products if all categories are selected', () => {
        expect(applyCategories(products, allCategories)).toEqual(products);
    });

    it('should uses filter and return products by categories', () => {
        expect(applyCategories(products, oneCategory)).toEqual([table]);
        expect(applyCategories(products, twoCategories)).toEqual([skirt, phone]);
    });
});
