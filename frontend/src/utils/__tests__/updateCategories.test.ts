import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('adds category', () => {
        const currentCategories: Category[] = ['Для дома', 'Одежда'];
        const changedCategories: Category = 'Электроника';
        const expected: Category[] = ['Для дома', 'Одежда', 'Электроника'];
        const actual = updateCategories(currentCategories, changedCategories);
        expect(actual).toEqual(expected);
    });

    it('delete category', () => {
        const currentCategories: Category[] = [
            'Для дома',
            'Одежда',
            'Электроника',
        ];
        const changedCategories: Category = 'Одежда';
        const expected: Category[] = ['Для дома', 'Электроника'];
        const actual = updateCategories(currentCategories, changedCategories);
        expect(actual).toEqual(expected);
    });
});
