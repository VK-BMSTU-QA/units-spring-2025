import { render, fireEvent } from '@testing-library/react';
import { MainPage } from './MainPage';
import { useProducts, useCurrentTime } from '../../hooks';

jest.mock('../../hooks/useProducts', () => ({
    useProducts: jest.fn(),
}));

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(),
}));

jest.mock('../../components', () => ({
    Categories: jest.fn(({ onCategoryClick }) => (
        <div>
            <button onClick={() => onCategoryClick()}>Электроника</button>
            <button onClick={() => onCategoryClick()}>Для дома</button>
            <button onClick={() => onCategoryClick()}>Одежда</button>
        </div>
    )),
    ProductCard: jest.fn(({ name }) => <div>{name}</div>),
}));

const Products = [{
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
] 

describe('test main page component', () => {
    beforeAll(() => {
        (useProducts as jest.Mock).mockReturnValue(Products);
        (useCurrentTime as jest.Mock).mockReturnValue('00:00');
    });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
        });

    it('filters products', () => {
       const rendered = render(<MainPage />);

        fireEvent.click(rendered.getByText('Электроника'));
        fireEvent.click(rendered.getByText('Для дома'));

        expect(rendered.queryByText('Костюм гуся')).toBeNull;
        expect(rendered.queryByText('Настольная лампа')).toBe;
        expect(rendered.queryByText('Принтер')).toBe;
        expect(rendered.queryByText('IPhone 14 Pro')).toBe;
    });
});
