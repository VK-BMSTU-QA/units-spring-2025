import { updateCategories } from '../updateCategories';
import { Category } from "../../types/Category";

describe('updateCategories function', () => {
    it('adds a new category when not present', () => {
        expect(updateCategories([], 'Электроника')).toEqual(['Электроника']);
    });

    it('removes an existing category when present', () => {
        expect(updateCategories(['Электроника'], 'Электроника')).toEqual([]);
    });

    it('toggles category in a multi-category list', () => {
        const current: Category[] = ['Электроника', 'Для дома'];
        expect(updateCategories(current, 'Электроника')).toEqual(['Для дома']);
        expect(updateCategories(current, 'Одежда')).toEqual([...current, 'Одежда']);
    });

    it('preserves order when removing from the middle', () => {
        const current: Category[] = ['Электроника', 'Для дома', 'Одежда'];
        expect(updateCategories(current, 'Для дома')).toEqual(['Электроника', 'Одежда']);
    });

    it('does not mutate the original array', () => {
        const original: Category[] = ['Электроника'];
        updateCategories(original, 'Электроника');
        expect(original).toHaveLength(1);
    });

    it('handles toggling with multiple additions', () => {
        let result = updateCategories([], 'Электроника');
        result = updateCategories(result, 'Для дома');
        result = updateCategories(result, 'Одежда');
        expect(result).toEqual(['Электроника', 'Для дома', 'Одежда']);
    });
});
