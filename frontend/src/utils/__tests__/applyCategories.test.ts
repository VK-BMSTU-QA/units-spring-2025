import { applyCategories } from '../applyCategories';
import { useProducts } from '../../hooks';
import { Category, Product } from '../../types';

describe('test apply categories function', () => {
    it('should return same produtcs if categories are empty', () => {
        expect(applyCategories(useProducts(), [])).toStrictEqual(useProducts());
    });

    it('should return all products if all categories are given', () => {
        const allCategories: Category[] = ['Для дома', 'Одежда', 'Электроника'];
        expect(applyCategories(useProducts(), allCategories)).toStrictEqual(useProducts());
    });

    it('should return products only with given categories', () => {
        const initialProducts: Product[] = useProducts();
        const categories: Category[] = ['Одежда'];
        const expectedProducts: Product[] = [initialProducts[1]];
        
        expect(applyCategories(initialProducts, categories)).toStrictEqual(expectedProducts);
    });
})
