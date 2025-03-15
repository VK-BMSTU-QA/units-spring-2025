import { render, cleanup, fireEvent } from '@testing-library/react'
import '@testing-library/jest-dom';
import { MainPage } from '../MainPage';
import type { Category, Product } from '../../../types';

const mockTime = '01:02:03';
const mockProducts = [
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
const mockCategory = 'Одежда' as Category;

jest.mock('../../../components/ProductCard', () => {
    return {
        ProductCard: jest.fn(({ name }: { name: String }) => <div data-testid={`product-card-${name}`} ></div >)
    }
});

jest.mock('../../../components/Categories', () => {
    return {
        Categories: jest.fn(({ onCategoryClick }) => <div data-testid='categories' onClick={() => onCategoryClick(mockCategory)}></div>)
    }
});

jest.mock('../../../hooks', () => {
    return {
        useCurrentTime: jest.fn(() => mockTime),
        useProducts: jest.fn(() => mockProducts),
    }
});

jest.mock('../../../utils', () => {
    return {
        applyCategories: jest.fn(() => mockProducts as Product[]),
        updateCategories: jest.fn(() => [mockCategory]),
    }
})

describe('testing main page component', () => {

    beforeEach(() => {
        jest.clearAllMocks();
    })

    afterEach(cleanup);

    it('renders', () => {
        const { asFragment } = render(<MainPage />);
        expect(asFragment()).toMatchSnapshot();
    })

    it('displays current time', () => {
        const { useCurrentTime } = jest.requireMock('../../../hooks/');

        const { container } = render(<MainPage />);

        expect(container.getElementsByTagName('h3').length).toBeGreaterThan(0);

        const timeElement = container.getElementsByTagName('h3')[0];

        expect(useCurrentTime).toHaveBeenCalled();
        expect(timeElement.innerHTML).toBe(mockTime);
    })

    it('displays product cards', () => {
        const { applyCategories } = jest.requireMock('../../../utils');
        const { useProducts } = jest.requireMock('../../../hooks');
        const { ProductCard } = jest.requireMock('../../../components/ProductCard');

        const rendered = render(<MainPage />);

        expect(useProducts).toBeCalled();
        expect(applyCategories).toBeCalledWith(mockProducts, []);
        expect(ProductCard).toBeCalledTimes(mockProducts.length);
        expect(ProductCard.mock.calls).toEqual(mockProducts.map((product) => [product, {}]));

        mockProducts.forEach(({ name }) => {
            expect(rendered.getByTestId(`product-card-${name}`)).toBeInTheDocument();
        })
    })

    it('renders categories', () => {
        const { Categories } = jest.requireMock('../../../components/Categories/');

        const rendered = render(<MainPage />);

        expect(Categories).toBeCalled();
        expect(rendered.getByTestId('categories')).toBeInTheDocument();
    });

    it('updates categories if they have been clicked', () => {
        const { Categories } = jest.requireMock('../../../components/Categories/');
        const { updateCategories } = jest.requireMock('../../../utils/');

        const rendered = render(<MainPage />);

        expect(rendered.getByTestId('categories')).toBeInTheDocument();
        const mockCategories = rendered.getByTestId('categories');

        fireEvent.click(mockCategories);

        expect(Categories).toBeCalledTimes(2);
        expect(Categories).toHaveBeenLastCalledWith(expect.objectContaining({
            selectedCategories: [mockCategory],
        }), {});
        expect(updateCategories).toBeCalled();
        expect(updateCategories).toHaveBeenLastCalledWith([], mockCategory);
    })
});
