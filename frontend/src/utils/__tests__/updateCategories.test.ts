import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

interface TestCase {
    name: string;
    input: {
        currentCategories: Category[];
        changedCategories: Category;
    };
    expectedOutput: Category[];
}

const testCases: TestCase[] = [
    {
        name: 'should add the category if it is not already included',
        input: {
            currentCategories: ['Электроника', 'Для дома'],
            changedCategories: 'Одежда',
        },
        expectedOutput: ['Электроника', 'Для дома', 'Одежда'],
    },
    {
        name: 'should remove the category if it is already included',
        input: {
            currentCategories: ['Электроника', 'Для дома', 'Одежда'],
            changedCategories: 'Одежда',
        },
        expectedOutput: ['Электроника', 'Для дома'],
    },
    {
        name: 'should add the category if the list is empty',
        input: {
            currentCategories: [],
            changedCategories: 'Электроника',
        },
        expectedOutput: ['Электроника'],
    },
];

describe('test update categories function', () => {
    testCases.forEach(({ name, input, expectedOutput }) => {
        it(name, () => {
            expect(
                updateCategories(
                    input.currentCategories,
                    input.changedCategories
                )
            ).toEqual(expectedOutput);
        });
    });
});
