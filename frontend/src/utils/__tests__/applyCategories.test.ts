import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

const products: Product[] = [
  {
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
  },
  {
    id: 2,
    name: 'Костюм гуся',
    description: 'Запускаем гуся, работяги',
    price: 1000,
    priceSymbol: '₽',
    category: 'Одежда',
  },
  {
    id: 3,
    name: 'Настольная лампа',
    description: 'Говорят, что ее использовали в pixar',
    price: 699,
    category: 'Для дома',
    imgUrl: '/lamp.png',
  },
  {
    id: 4,
    name: 'Принтер',
    description: 'Незаменимая вещь для студента',
    price: 7000,
    category: 'Электроника',
  },
];

describe('applyCategories empty list of categories', () => {
  type TestCase = {
    input: Category[]
    want: Product[]
  }

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
  ]

  const runTest = (selectedCategories: Category[], expected: Product[]) => {
    const result = applyCategories(products, selectedCategories);
    expect(result).toStrictEqual(expected);
  };
  
  test.each<TestCase>(tests)('categories applied correctly', ({input, want}) => {
    runTest(input, want);
  });
});