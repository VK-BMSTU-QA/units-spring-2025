import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('Testing select in updateCategories', () => {
    const runTest = (
        selectedCategories: Category[],
        newCategory: Category,
        expected: Category[]
    ) => {
        const result = updateCategories(selectedCategories, newCategory);
        expect(result).toEqual(expected);
    };

    test.each([
        [[] as Category[], 'Одежда' as Category, ['Одежда'] as Category[]],
        [
            ['Одежда'] as Category[],
            'Для дома' as Category,
            ['Одежда', 'Для дома'] as Category[],
        ],
    ])(
        'should select categories correctly',
        (selectedCategories, newCategory, expected) => {
            runTest(selectedCategories, newCategory, expected);
        }
    );
});

describe('Testing remove in updateCategories', () => {
    const runTest = (
        selectedCategories: Category[],
        newCategory: Category,
        expected: Category[]
    ) => {
        const result = updateCategories(selectedCategories, newCategory);
        expect(result).toEqual(expected);
    };

    test.each([
        [
            ['Одежда', 'Для дома', 'Электроника'] as Category[],
            'Для дома' as Category,
            ['Одежда', 'Электроника'] as Category[],
        ],
        [['Одежда'] as Category[], 'Одежда' as Category, [] as Category[]],
    ])(
        'should remove categories correctly',
        (selectedCategories, newCategory, expected) => {
            runTest(selectedCategories, newCategory, expected);
        }
    );
});

