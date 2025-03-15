import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime } from '../../hooks';

afterEach(jest.clearAllMocks);
const categories = ['Одежда', 'Для дома', 'Электроника'];
const products = [
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


describe('Main page test', () => {
    afterEach(() => { jest.restoreAllMocks() });
    it('should render correctly', () => {
        const defTime = new Date(1, 1, 1, 1, 0, 0)
        jest.spyOn(global, 'Date').mockImplementation(() => defTime);
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