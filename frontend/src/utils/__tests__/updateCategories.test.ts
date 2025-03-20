import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('Test updateCategories', () => {
    it('removes category', () => {
        const categories: Category[] = ['Электроника'];
        const toChange: Category = 'Электроника';
        const expected: Category[] = [];
        const actual = updateCategories(categories, toChange);
        expect(actual).toEqual(expected);
    });
    it('adds category', () => {
        const categories: Category[] = ['Электроника'];
        const toChange: Category = 'Для дома';
        const expected: Category[] = ['Электроника', 'Для дома'];
        const actual = updateCategories(categories, toChange);
        expect(actual).toEqual(expected);
    });
});
