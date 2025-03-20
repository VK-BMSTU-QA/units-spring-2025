import { fireEvent, render } from '@testing-library/react';
import React from 'react';
import { MainPage } from '../MainPage';
import { Product } from '../../types';
import '@testing-library/jest-dom/extend-expect';

const testProducts: Product[] = [
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

describe('Test MainPage component', () => {
    it('renders as in shapshot', () => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date('1995-12-17T03:24:00'));

        jest.mock('../../hooks', () => {
            return {
                useProducts: jest.fn().mockReturnValue(testProducts),
            };
        });

        const r = render(<MainPage />);
        expect(r.asFragment()).toMatchSnapshot();
    });

    it('does not show irrelevant item when filters are active', () => {
        jest.mock('../../hooks', () => {
            return {
                useProducts: jest.fn().mockReturnValue(testProducts),
            };
        });

        const r = render(<MainPage />);
        expect(r.asFragment()).toHaveTextContent('IPhone 14 Pro');
        fireEvent.click(r.getAllByText('Для дома')[0]);
        expect(r.asFragment()).not.toHaveTextContent('IPhone 14 Pro');
    });

    it('shows relevant item when filters are active', () => {
        jest.mock('../../hooks', () => {
            return {
                useProducts: jest.fn().mockReturnValue(testProducts),
            };
        });

        const r = render(<MainPage />);
        expect(r.asFragment()).toHaveTextContent('IPhone 14 Pro');
        fireEvent.click(r.getAllByText('Электроника')[0]);
        expect(r.asFragment()).toHaveTextContent('IPhone 14 Pro');
    });

    it('disables active filter on click', () => {
        jest.mock('../../hooks', () => {
            return {
                useProducts: jest.fn().mockReturnValue(testProducts),
            };
        });

        const r = render(<MainPage />);
        expect(r.asFragment()).toHaveTextContent('IPhone 14 Pro');
        fireEvent.click(r.getAllByText('Для дома')[0]);
        expect(r.asFragment()).not.toHaveTextContent('IPhone 14 Pro');
        fireEvent.click(r.getAllByText('Для дома')[0]);
        expect(r.asFragment()).toHaveTextContent('IPhone 14 Pro');
    });
});
