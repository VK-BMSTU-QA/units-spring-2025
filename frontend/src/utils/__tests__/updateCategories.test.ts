import { updateCategories } from '../../utils';
import type { Category } from '../../types';

describe('updateCategories', () => {
    it('should add a new category if it is not already present', () => {
        const currentCategories: Category[] = ['Для дома', 'Электроника'];
        const changedCategory: Category = 'Одежда';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual([...currentCategories, changedCategory]);
    });

    it('should remove a category if it is already present', () => {
        const currentCategories: Category[] = ['Для дома', 'Электроника'];
        const changedCategory: Category = 'Электроника';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Для дома']);
    });

    it('should not modify the categories if the category is already in the list and no change is made', () => {
        const currentCategories: Category[] = ['Для дома', 'Одежда'];
        const changedCategory: Category = 'Одежда';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Для дома']);
    });
});
