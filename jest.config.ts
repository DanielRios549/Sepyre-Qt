import type { Config } from '@jest/types'

const config: Config.InitialOptions = {
    preset: 'ts-jest',
    verbose: true,
    collectCoverage: true,
    collectCoverageFrom: [
        'pages/*.{svelte}',
        'src/**/*.{ts,svelte}',
        '!src/**/*.d.ts'
    ],
    transform: {
        '^.+\\.tsx?$': 'ts-jest'
    },
    moduleNameMapper: {
        '\\$/(.*)': '<rootDir>/src/$1'
    }
}

export default config
