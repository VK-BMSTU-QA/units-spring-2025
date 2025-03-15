import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('updateCategories test', () => {
    it('should add a new category if it is not in the current list', () => {
        const currentCategories: Category[] = ['Электроника', 'Одежда'];
        const changedCategory: Category = 'Для дома';

        const result = updateCategories(currentCategories, changedCategory);

        expect(result).toHaveLength(3);
        expect(result).toEqual([...currentCategories, changedCategory]);
    });

    it('should remove a category if it is already in the current list', () => {
        const currentCategories: Category[] = [
            'Электроника',
            'Одежда',
            'Для дома',
        ];
        const changedCategory: Category = 'Одежда';

        const result = updateCategories(currentCategories, changedCategory);

        expect(result).toHaveLength(2);
        expect(result).toEqual(['Электроника', 'Для дома']);
    });

    it('should handle an empty list of current categories', () => {
        const currentCategories: Category[] = [];
        const changedCategory: Category = 'Электроника';

        const result = updateCategories(currentCategories, changedCategory);

        expect(result).toHaveLength(1);
        expect(result).toEqual([changedCategory]);
    });

    it('should handle removing the last category', () => {
        const currentCategories: Category[] = ['Электроника'];
        const changedCategory: Category = 'Электроника';

        const result = updateCategories(currentCategories, changedCategory);

        expect(result).toHaveLength(0);
        expect(result).toEqual([]);
    });
});
