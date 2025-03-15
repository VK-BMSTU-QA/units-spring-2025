import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    type TestCase = {
        currentCategories: Category[];
        changedCategories: Category;
        expected: Category[];
    };
    
    const testCases: TestCase[] = [
        {
            currentCategories: [],
            changedCategories: 'Для дома',
            expected: ['Для дома'],
        },
        {
            currentCategories: ['Одежда'],
            changedCategories: 'Одежда',
            expected: [],
        },
        {
            currentCategories: ['Одежда', 'Для дома', 'Электроника'],
            changedCategories: 'Одежда',
            expected: ['Для дома', 'Электроника'],
        },
        {
            currentCategories: ['Одежда', 'Для дома'],
            changedCategories: 'Электроника',
            expected: ['Одежда', 'Для дома', 'Электроника'],
        },
    ];
    
    test.each<TestCase>(testCases)('updateCategories(%s, %s)', ({ currentCategories, changedCategories, expected }) => {
        expect(updateCategories(currentCategories as Category[], changedCategories as Category)).toStrictEqual(expected);
    });
});
