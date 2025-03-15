import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';
import { getProducts } from '../../mocks/productMocks';

describe('applyCategories empty list of categories', () => {
  const products: Product[] = getProducts();
  type TestCase = {
    input: Category[]
    want: Product[]
  };

  const tests: TestCase[] = [
    {
      input: [] as Category[],
      want: products,
    },
    {
      input: ['Одежда', 'Для дома', 'Электроника'] as Category[],
      want: products,
    },
    {
      input: ['Электроника'] as Category[],
      want: [products[0], products[3]],
    },
    {
      input: ['Одежда'] as Category[],
      want: [products[1]],
    },
    {
      input: ['Одежда', 'Для дома'] as Category[],
      want: [products[1], products[2]],
    },
  ];

  const runTest = (selectedCategories: Category[], expected: Product[]) => {
    const result = applyCategories(products, selectedCategories);
    expect(result).toStrictEqual(expected);
  };
  
  test.each<TestCase>(tests)('categories applied correctly', ({input, want}) => {
    runTest(input, want);
  });
});