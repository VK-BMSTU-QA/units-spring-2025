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
        useProducts: () => products,
    }
});

describe('Main page test', () => {
    afterEach(() => { jest.restoreAllMocks() });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should correct categories', () => {
        categories.forEach((category) => {
            const rendered = render(<MainPage></MainPage>);
            const categoryBadge = rendered.getByText(category, {
                selector: '.categories__badge',
            });
            fireEvent.click(categoryBadge);
            products.forEach((product) => {
                if (product.category === category) {
                    expect(
                        rendered.getByText(product.name)
                    ).toBeInTheDocument();
                } else {
                    expect(
                        rendered.queryByText(product.name)
                    ).not.toBeInTheDocument();
                }
            });
            rendered.unmount();
        });
    });
});