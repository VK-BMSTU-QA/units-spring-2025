import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test applyCategories function', () => {
    const testCases = [
        { 
            currentCategories: [], 
            changedCategories: 'Одежда', 
            expected: ['Одежда'] 
        },
        { 
            currentCategories: ['Одежда'], 
            changedCategories: 'Одежда', 
            expected: [] 
            
        },
        { 
            currentCategories: ['Одежда', 'Для дома'], 
            changedCategories: 'Электроника', 
            expected: ['Одежда', 'Для дома', 'Электроника'] 
        },
        { 
            currentCategories: ['Одежда', 'Для дома', 'Электроника'], 
            changedCategories: 'Одежда', 
            expected: ['Для дома', 'Электроника'] 
        },
    ];

    test.each(testCases)(
        'updateCategories(%s, %s) should return %s',
        ({ currentCategories, changedCategories, expected }) => {
            expect(updateCategories(currentCategories as Category[], changedCategories as Category)).toStrictEqual(expected);
        }
    );
});
