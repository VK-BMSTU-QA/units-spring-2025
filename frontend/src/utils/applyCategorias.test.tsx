import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { applyCategories } from './applyCategories';
afterEach(jest.clearAllMocks);
import type { Category, Product } from '../types';
import { Categories } from '../components';

describe("applyCategories testing", () => {
    const testProducts: Product[] = [
        {
            id: 1,
            name: 'Ноутбук',
            description: 'Мощный ноутбук для работы и игр',
            price: 1500,
            priceSymbol: '$',
            imgUrl: 'https://example.com/laptop.jpg',
            category: 'Электроника' as Category,
        },
        {
            id: 2,
            name: 'Футболка',
            description: 'Мягкая и удобная футболка',
            price: 20,
            priceSymbol: '$',
            imgUrl: 'https://example.com/tshirt.jpg',
            category: 'Одежда' as Category,
        },
        {
            id: 3,
            name: 'Кофеварка',
            description: 'Автоматическая кофеварка для дома',
            price: 80,
            priceSymbol: '₽',
            imgUrl: 'https://example.com/coffee-maker.jpg',
            category: 'Для дома' as Category,
        },
        {
            id: 4,
            name: 'Смартфон',
            description: 'Современный смартфон с большим экраном',
            price: 800,
            priceSymbol: '$',
            category: 'Электроника' as Category, // imgUrl отсутствует
        },
        ];


    it("Check update with two", () => {
        expect(applyCategories(testProducts, ['Одежда'] as Category[])).toBe([ {
            id: 2,
            name: 'Футболка',
            description: 'Мягкая и удобная футболка',
            price: 20,
            priceSymbol: '€',
            imgUrl: 'https://example.com/tshirt.jpg',
            category: 'Одежда' as Category,
        }, ]);
    })

    it("Check update with two", () => {
        expect(applyCategories(testProducts, [] as Category[])).toBe(testProducts);
    })

    it("Check update with two", () => {
        expect(applyCategories(testProducts, ['Одежда', 'Электроника'] as Category[])).toBe([{
            id: 1,
            name: 'Ноутбук',
            description: 'Мощный ноутбук для работы и игр',
            price: 1500,
            priceSymbol: '$',
            imgUrl: 'https://example.com/laptop.jpg',
            category: 'Электроника' as Category,
        },
        {
            id: 2,
            name: 'Футболка',
            description: 'Мягкая и удобная футболка',
            price: 20,
            priceSymbol: '$',
            imgUrl: 'https://example.com/tshirt.jpg',
            category: 'Одежда' as Category,
        }, 
        {
            id: 4,
            name: 'Смартфон',
            description: 'Современный смартфон с большим экраном',
            price: 800,
            priceSymbol: '$',
            category: 'Электроника' as Category,
        },]);
    })
})