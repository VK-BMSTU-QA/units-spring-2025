import React from 'react';
import { render, fireEvent, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import type { Product, Category } from '../../types';

const someProducts = [
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
] as Product[];


jest.mock('../../hooks', () => {
    return {
        useCurrentTime: jest.fn(() => new Date(2004, 9, 12, 20).toLocaleTimeString('ru-RU')),
        useProducts: jest.fn(() => someProducts),
    }
  });



afterEach(jest.clearAllMocks);

describe('MainPage test', () => {

    beforeEach(() => {
        jest.clearAllMocks();
    })

    afterEach(cleanup);

    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    }); 

    it('should add 1 to count', () => {
        const rendered = render(<MainPage />)
        const category = rendered.getAllByText('Одежда')

        fireEvent.click(category[0])
        expect(category[0]).toHaveClass('categories__badge_selected')
    })

    it('current time', () => {
        const { container } = render(<MainPage />);
        const timeElement = container.getElementsByTagName('h3')[0];
        expect(timeElement.innerHTML).toBe("20:00:00");
    })
});
