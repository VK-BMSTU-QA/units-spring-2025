import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test apply categories function', () => {
    const currentCategories : Category[] = ["Одежда", "Для дома"];
    const newCategory : Category = "Электроника";
    const existedCategory : Category = 'Одежда';

    it('should add new category', () => {
        const updatedCategories = updateCategories(currentCategories, newCategory);
        expect(updatedCategories).toContain(newCategory);
    });

    it('should remove existed category', () => {
        const updatedCategories = updateCategories(currentCategories, existedCategory);
        expect(updatedCategories).not.toContain(existedCategory);
    });
});