import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

const categories = ['Электроника']

describe('test update category function', () => {
    it('should return value with price symbol', () => {
        expect(updateCategories(['Электроника', 'Одежда'], 'Одежда')).toStrictEqual(['Электроника']);
        expect(updateCategories(['Электроника', 'Одежда'], 'Для дома')).toBe(['Электроника', 'Одежда', 'Для дома']);
    });
});