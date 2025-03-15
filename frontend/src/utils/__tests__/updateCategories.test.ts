import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    it('should exclude changed categories from current categories if they contain them', () => {
        const currentCategories: Category[] = ['Для дома', 'Одежда', 'Электроника'];
        const changedCategories: Category = 'Электроника';
        const expectedCategories: Category[] = ['Для дома', 'Одежда'];

        expect(updateCategories(currentCategories, changedCategories)).toStrictEqual(expectedCategories);
    });

    it('should add changed categories to current categories if they dont contain them', () => {
        const currentCategories: Category[] = ['Для дома', 'Одежда'];
        const changedCategories: Category = 'Электроника';
        const expectedCategories: Category[] = ['Для дома', 'Одежда', 'Электроника'];

        expect(updateCategories(currentCategories, changedCategories)).toStrictEqual(expectedCategories);
    })

    it('should exclude changed categories from current categories even if there is only one current category', () => {
        const currentCategories: Category[] = ['Для дома'];
        const changedCategories: Category = 'Для дома';
        const expectedCategories: Category[] = [];

        expect(updateCategories(currentCategories, changedCategories)).toStrictEqual(expectedCategories);
    })
});
