import { updateCategories } from '../updateCategories';
import {Category} from '../../types';

const Categories: Category[] = [ 'Электроника', 'Для дома' , 'Одежда'];

describe('test get price function', () => {
    it('should return updated categories', () => {
        expect(updateCategories(Categories, Categories[0] )).toEqual([Categories[1], Categories[2]]);
    });
    it('should return updated categories', () => {
        expect(updateCategories([Categories[1], Categories[2]], Categories[0] )).toEqual([Categories[1], Categories[2], Categories[0]]);
    });
});
