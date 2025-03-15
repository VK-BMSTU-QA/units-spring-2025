import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return updated categories', () => {
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
        expect(updateCategories(['Одежда'], 'Для дома')).toStrictEqual(['Одежда', 'Для дома'])
        expect(updateCategories(['Электроника', 'Электроника', 'Одежда', 'Одежда'], 'Для дома')).
            toStrictEqual(['Электроника', 'Электроника', 'Одежда', 'Одежда', 'Для дома'])
    });
    it('should delete category', () => {
        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([])
        expect(updateCategories(['Электроника', 'Для дома', 'Одежда'], 'Для дома')).
            toStrictEqual(['Электроника', 'Одежда'])
        expect(updateCategories(['Электроника', 'Для дома', 'Одежда', 'Одежда', 'Одежда'], 'Одежда')).
            toStrictEqual(['Электроника', 'Для дома'])
    });
});