import { applyCategories } from '../applyCategories';
import { Product } from "../../types/Product";
import { Category } from "../../types/Category";

const products: Product[] = [
    { id: 1, name: 'Телефон', description: 'test', category: 'Электроника', price: 100 },
    { id: 2, name: 'Стол', description: 'test', category: 'Для дома', price: 200 },
    { id: 3, name: 'Футболка', description: 'test', category: 'Одежда', price: 50 },
    { id: 4, name: 'Ноутбук', description: 'test', category: 'Электроника', price: 1000 },
];

describe('applyCategories function', () => {
    it('returns all products when categories are empty', () => {
        expect(applyCategories(products, [])).toEqual(products);
    });

    it('filters products by a single category', () => {
        const filtered = applyCategories(products, ['Электроника']);
        expect(filtered).toEqual([products[0], products[3]]);
    });

    it('filters products by multiple categories', () => {
        const filtered = applyCategories(products, ['Электроника', 'Одежда']);
        expect(filtered).toEqual([products[0], products[2], products[3]]);
    });

    it('does not mutate the original products array', () => {
        applyCategories(products, ['Электроника']);
        expect(products).toHaveLength(4);
    });

    it('handles case with all products filtered out', () => {
        const filtered = applyCategories(products, ['Для дома', 'Одежда']);
        expect(filtered).toEqual([products[1], products[2]]);
    });
});
