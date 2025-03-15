import { applyCategories } from '../applyCategories';
import type { Category, Product } from '../../types';

describe('applyCategories test', () => {
    let products: Product[];

    beforeEach(() => {
        products = [
            {
                category: 'Электроника',
            },
            {
                category: 'Одежда',
            },
            {
                category: 'Для дома',
            },
            {
                category: 'Электроника',
            },
        ] as Product[];
    });

    it('should filter products by one category (Электроника)', () => {
        const categories: Category[] = ['Электроника'];
        const result = applyCategories(products, categories);

        expect(result).toEqual([products[0], products[3]]);
    });

    it('should filter products by multiple categories (Электроника, Одежда)', () => {
        const categories: Category[] = ['Электроника', 'Одежда'];
        const result = applyCategories(products, categories);

        expect(result).toEqual([products[0], products[1], products[3]]);
    });

    it('should return all products if all categories are selected', () => {
        const categories: Category[] = ['Электроника', 'Одежда', 'Для дома'];
        const result = applyCategories(products, categories);

        expect(result).toEqual(products);
    });

    it('should return all products if no categories are selected', () => {
        const categories: Category[] = [];
        const result = applyCategories(products, categories);

        expect(result).toEqual(products);
    });

    it('should return empty array if no products match the selected categories', () => {
        const categories: Category[] = ['Одежда', 'Электроника'];
        const filteredProducts = products.filter(
            (p) => p.category === 'Для дома'
        );
        const result = applyCategories(filteredProducts, categories);

        expect(result).toEqual([]);
    });
});
