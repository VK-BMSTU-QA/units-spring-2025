import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('test update categories function', () => {

    it.each([
        [[], 'Для дома', ['Для дома']],
        [['Электроника'], 'Одежда', ['Электроника', 'Одежда']],
        [['Одежда'], 'Для дома', ['Одежда', 'Для дома']]])
        (`adds to the current categories %p new one %p `, (currentCategories, changedCategory, expected) => {
            expect(updateCategories(currentCategories as Category[], changedCategory as Category)).toStrictEqual(expected);
        });

    it.each([
        [['Для дома'], 'Для дома', []],
        [['Для дома', 'Одежда'], 'Для дома', ['Одежда']],
        [['Одежда', 'Для дома', 'Электроника'], 'Одежда', ['Для дома', 'Электроника']]])
        (`removes from current categories %p provided one %p if it is in current`, (currentCategories, changedCategory, expected) => {
            expect(updateCategories(currentCategories as Category[], changedCategory as Category)).toStrictEqual(expected);
        });
})
