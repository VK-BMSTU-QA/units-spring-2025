import { updateCategories } from '../updateCategories';

describe('test updateCategories function', () => {
    it('should add new category', () => {
        expect(updateCategories([], 'Для дома')).toEqual(['Для дома']);
        expect(updateCategories(['Электроника'], 'Одежда')).toEqual([
            'Электроника',
            'Одежда',
        ]);
    });

    it('should remove existing category', () => {
        expect(updateCategories(['Одежда', 'Для дома'], 'Одежда')).toEqual([
            'Для дома',
        ]);
        expect(
            updateCategories(
                ['Одежда', 'Электроника', 'Для дома'],
                'Электроника'
            )
        ).toEqual(['Одежда', 'Для дома']);
        expect(
            updateCategories(
                ['Одежда', 'Для дома', 'Одежда', 'Электроника'],
                'Одежда'
            )
        ).toEqual(['Для дома', 'Электроника']);
    });
});
