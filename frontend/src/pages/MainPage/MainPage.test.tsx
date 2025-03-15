import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import type { Product } from '../../types';

afterEach(jest.clearAllMocks);
const categories = ['Одежда', 'Для дома', 'Электроника'];
const products = [
    {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 1,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    },
    {
        id: 2,
        name: 'Костюм гуся',
        description: 'Запускаем гуся, работяги',
        price: 1,
        priceSymbol: '$',
        category: 'Одежда',
    },
    {
        id: 3,
        name: 'Настольная лампа',
        description: 'Говорят, что ее использовали в pixar',
        price: 1,
        priceSymbol: '$',
        category: 'Для дома',
        imgUrl: '/lamp.png',
    },
    {
        id: 4,
        name: 'Принтер',
        description: 'Незаменимая вещь для студента',
        price: 1,
        priceSymbol: '$',
        category: 'Электроника',
    },
] as Product[];

jest.mock('../../hooks', () => {
    return {
        useCurrentTime: jest.fn(() => '1:00:00'),
        useProducts: jest.fn(() => products),
    }
});

jest.mock('../../utils', () => {
    return {
        applyCategories: jest.fn(() => products as Product[]),
        updateCategories: jest.fn(() => [categories]),
        getPrice: jest.fn(() => '1 $')
    }
})

describe('Main page test', () => {
    afterEach(() => { jest.restoreAllMocks() });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should correct categories called', () => {
        const { useCurrentTime } = jest.requireMock('../../hooks/');
        const { useProducts } = jest.requireMock('../../hooks');
        const { applyCategories } = jest.requireMock('../../utils');
        const { updateCategories } = jest.requireMock('../../utils');
        categories.forEach((category) => {
            const rendered = render(<MainPage></MainPage>);
            const categoryBadge = rendered.getByText(category, {
                selector: '.categories__badge',
            });
            fireEvent.click(categoryBadge);
            expect(useProducts).toBeCalled();
            expect(useCurrentTime).toBeCalled();
            expect(applyCategories).toBeCalled();
            expect(updateCategories).toBeCalled();
            rendered.unmount();
        });
    });
});