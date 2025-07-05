# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.90</td>
    <td align="right">6.36</td>
    <td align="right">4.34</td>
    <td align="right">12.92</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">9.97</td>
    <td align="right">11.48</td>
    <td align="right">19.55</td>
    <td align="right">16.42</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.98</td>
    <td align="right">4.16</td>
    <td align="right">4.51</td>
    <td align="right">10.77</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.42</td>
    <td align="right">4.64</td>
    <td align="right">4.83</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.85</td>
    <td align="right">17.39</td>
    <td align="right">20.73</td>
    <td align="right">20.26</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.35</td>
    <td align="right">4.75</td>
    <td align="right">4.64</td>
    <td align="right">11.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.05</td>
    <td align="right">5.18</td>
    <td align="right">5.08</td>
    <td align="right">11.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.60</td>
    <td align="right">21.07</td>
    <td align="right">20.21</td>
    <td align="right">23.42</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.23</td>
    <td align="right">5.05</td>
    <td align="right">12.07</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.52</td>
    <td align="right">5.71</td>
    <td align="right">5.44</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.59</td>
    <td align="right">27.30</td>
    <td align="right">20.30</td>
    <td align="right">27.07</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.76</td>
    <td align="right">5.46</td>
    <td align="right">12.42</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.94</td>
    <td align="right">6.08</td>
    <td align="right">5.88</td>
    <td align="right">12.84</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">9.97</td>
    <td align="right">13.22</td>
    <td align="right">12.98</td>
    <td align="right">19.70</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.98</td>
    <td align="right">4.16</td>
    <td align="right">4.51</td>
    <td align="right">10.78</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.42</td>
    <td align="right">4.64</td>
    <td align="right">4.83</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.95</td>
    <td align="right">20.69</td>
    <td align="right">16.22</td>
    <td align="right">25.89</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.35</td>
    <td align="right">4.77</td>
    <td align="right">4.63</td>
    <td align="right">11.37</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.21</td>
    <td align="right">5.17</td>
    <td align="right">5.07</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.45</td>
    <td align="right">25.94</td>
    <td align="right">20.02</td>
    <td align="right">32.35</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.23</td>
    <td align="right">5.06</td>
    <td align="right">12.16</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.51</td>
    <td align="right">5.71</td>
    <td align="right">5.44</td>
    <td align="right">12.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.70</td>
    <td align="right">32.00</td>
    <td align="right">25.32</td>
    <td align="right">38.98</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.36</td>
    <td align="right">5.72</td>
    <td align="right">5.43</td>
    <td align="right">12.38</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.95</td>
    <td align="right">6.08</td>
    <td align="right">5.89</td>
    <td align="right">12.85</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">4.69</td>
    <td align="right">5.69</td>
    <td align="right">14.87</td>
    <td align="right">12.39</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.52</td>
    <td align="right">7.16</td>
    <td align="right">14.69</td>
    <td align="right">13.08</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.96</td>
    <td align="right">3.25</td>
    <td align="right">3.68</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.11</td>
    <td align="right">8.49</td>
    <td align="right">15.52</td>
    <td align="right">14.33</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.85</td>
    <td align="right">9.32</td>
    <td align="right">16.54</td>
    <td align="right">15.21</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.58</td>
    <td align="right">3.12</td>
    <td align="right">3.07</td>
    <td align="right">11.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.59</td>
    <td align="right">11.97</td>
    <td align="right">16.28</td>
    <td align="right">17.06</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.17</td>
    <td align="right">11.95</td>
    <td align="right">16.82</td>
    <td align="right">17.65</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.27</td>
    <td align="right">6.02</td>
    <td align="right">3.86</td>
    <td align="right">14.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.12</td>
    <td align="right">13.68</td>
    <td align="right">15.58</td>
    <td align="right">19.28</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.50</td>
    <td align="right">14.26</td>
    <td align="right">17.57</td>
    <td align="right">19.14</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.32</td>
    <td align="right">6.06</td>
    <td align="right">3.84</td>
    <td align="right">14.91</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">4.68</td>
    <td align="right">5.86</td>
    <td align="right">5.94</td>
    <td align="right">12.23</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.49</td>
    <td align="right">7.10</td>
    <td align="right">7.15</td>
    <td align="right">13.53</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.95</td>
    <td align="right">3.26</td>
    <td align="right">3.67</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.10</td>
    <td align="right">8.15</td>
    <td align="right">8.09</td>
    <td align="right">14.25</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.82</td>
    <td align="right">9.35</td>
    <td align="right">9.24</td>
    <td align="right">16.66</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.56</td>
    <td align="right">3.14</td>
    <td align="right">3.08</td>
    <td align="right">12.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.56</td>
    <td align="right">11.15</td>
    <td align="right">10.89</td>
    <td align="right">16.87</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.17</td>
    <td align="right">11.96</td>
    <td align="right">11.79</td>
    <td align="right">18.74</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.26</td>
    <td align="right">5.49</td>
    <td align="right">5.39</td>
    <td align="right">14.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.11</td>
    <td align="right">12.35</td>
    <td align="right">12.25</td>
    <td align="right">18.23</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.49</td>
    <td align="right">14.61</td>
    <td align="right">14.55</td>
    <td align="right">21.48</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.31</td>
    <td align="right">5.56</td>
    <td align="right">5.39</td>
    <td align="right">14.39</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.92</td>
    <td align="right">3.04</td>
    <td align="right">3.40</td>
    <td align="right">11.50</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.45</td>
    <td align="right">4.52</td>
    <td align="right">4.85</td>
    <td align="right">14.67</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.65</td>
    <td align="right">4.32</td>
    <td align="right">4.61</td>
    <td align="right">14.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.06</td>
    <td align="right">3.13</td>
    <td align="right">3.03</td>
    <td align="right">12.09</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.46</td>
    <td align="right">4.19</td>
    <td align="right">4.00</td>
    <td align="right">14.23</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.57</td>
    <td align="right">4.44</td>
    <td align="right">4.37</td>
    <td align="right">14.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.45</td>
    <td align="right">5.61</td>
    <td align="right">3.69</td>
    <td align="right">14.37</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.32</td>
    <td align="right">7.99</td>
    <td align="right">5.91</td>
    <td align="right">17.70</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.47</td>
    <td align="right">7.90</td>
    <td align="right">5.90</td>
    <td align="right">17.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.51</td>
    <td align="right">5.64</td>
    <td align="right">3.66</td>
    <td align="right">14.97</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.02</td>
    <td align="right">9.14</td>
    <td align="right">5.97</td>
    <td align="right">19.29</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.71</td>
    <td align="right">8.93</td>
    <td align="right">5.91</td>
    <td align="right">18.55</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.91</td>
    <td align="right">3.05</td>
    <td align="right">3.42</td>
    <td align="right">11.85</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.44</td>
    <td align="right">4.51</td>
    <td align="right">4.83</td>
    <td align="right">14.65</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.63</td>
    <td align="right">4.31</td>
    <td align="right">4.62</td>
    <td align="right">14.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.03</td>
    <td align="right">3.10</td>
    <td align="right">3.02</td>
    <td align="right">11.92</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.43</td>
    <td align="right">4.22</td>
    <td align="right">3.97</td>
    <td align="right">13.96</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.59</td>
    <td align="right">4.43</td>
    <td align="right">4.26</td>
    <td align="right">14.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.44</td>
    <td align="right">5.34</td>
    <td align="right">5.15</td>
    <td align="right">13.82</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.26</td>
    <td align="right">7.60</td>
    <td align="right">7.21</td>
    <td align="right">16.42</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.43</td>
    <td align="right">7.50</td>
    <td align="right">7.12</td>
    <td align="right">15.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.50</td>
    <td align="right">5.35</td>
    <td align="right">5.16</td>
    <td align="right">13.85</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.97</td>
    <td align="right">8.27</td>
    <td align="right">8.23</td>
    <td align="right">16.83</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.69</td>
    <td align="right">8.22</td>
    <td align="right">8.13</td>
    <td align="right">16.44</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.41</td>
    <td align="right">7.25</td>
    <td align="right">14.95</td>
    <td align="right">13.17</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.23</td>
    <td align="right">8.53</td>
    <td align="right">18.69</td>
    <td align="right">16.08</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.09</td>
    <td align="right">10.61</td>
    <td align="right">19.14</td>
    <td align="right">16.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.08</td>
    <td align="right">10.11</td>
    <td align="right">14.59</td>
    <td align="right">17.02</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.61</td>
    <td align="right">10.18</td>
    <td align="right">15.87</td>
    <td align="right">17.12</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">12.83</td>
    <td align="right">14.34</td>
    <td align="right">19.25</td>
    <td align="right">18.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.09</td>
    <td align="right">11.61</td>
    <td align="right">13.85</td>
    <td align="right">16.83</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.35</td>
    <td align="right">12.73</td>
    <td align="right">17.02</td>
    <td align="right">19.49</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.09</td>
    <td align="right">15.47</td>
    <td align="right">16.99</td>
    <td align="right">19.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.24</td>
    <td align="right">14.31</td>
    <td align="right">15.07</td>
    <td align="right">18.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.65</td>
    <td align="right">14.85</td>
    <td align="right">16.72</td>
    <td align="right">20.06</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.19</td>
    <td align="right">19.66</td>
    <td align="right">18.17</td>
    <td align="right">22.48</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.42</td>
    <td align="right">7.24</td>
    <td align="right">7.32</td>
    <td align="right">13.49</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.21</td>
    <td align="right">8.80</td>
    <td align="right">8.91</td>
    <td align="right">15.95</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.02</td>
    <td align="right">10.77</td>
    <td align="right">11.00</td>
    <td align="right">17.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.10</td>
    <td align="right">10.08</td>
    <td align="right">10.05</td>
    <td align="right">16.43</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.68</td>
    <td align="right">10.98</td>
    <td align="right">10.90</td>
    <td align="right">17.87</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.78</td>
    <td align="right">14.25</td>
    <td align="right">14.18</td>
    <td align="right">21.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.10</td>
    <td align="right">11.42</td>
    <td align="right">11.61</td>
    <td align="right">17.85</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.35</td>
    <td align="right">13.99</td>
    <td align="right">13.18</td>
    <td align="right">20.43</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.14</td>
    <td align="right">16.04</td>
    <td align="right">15.74</td>
    <td align="right">22.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.26</td>
    <td align="right">14.40</td>
    <td align="right">14.33</td>
    <td align="right">19.85</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.61</td>
    <td align="right">15.92</td>
    <td align="right">15.88</td>
    <td align="right">21.55</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.60</td>
    <td align="right">20.05</td>
    <td align="right">19.70</td>
    <td align="right">25.81</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.83</td>
    <td align="right">25.74</td>
    <td align="right">14.45</td>
    <td align="right">32.49</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.60</td>
    <td align="right">17.06</td>
    <td align="right">23.12</td>
    <td align="right">20.52</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.17</td>
    <td align="right">6.40</td>
    <td align="right">6.75</td>
    <td align="right">12.93</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.91</td>
    <td align="right">6.31</td>
    <td align="right">6.42</td>
    <td align="right">12.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">49.72</td>
    <td align="right">57.44</td>
    <td align="right">30.77</td>
    <td align="right">44.42</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.36</td>
    <td align="right">11.21</td>
    <td align="right">10.67</td>
    <td align="right">16.58</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.64</td>
    <td align="right">11.91</td>
    <td align="right">11.75</td>
    <td align="right">17.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">78.18</td>
    <td align="right">93.17</td>
    <td align="right">36.01</td>
    <td align="right">65.69</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.54</td>
    <td align="right">17.65</td>
    <td align="right">17.45</td>
    <td align="right">22.74</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.28</td>
    <td align="right">20.10</td>
    <td align="right">18.12</td>
    <td align="right">23.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.42</td>
    <td align="right">135.97</td>
    <td align="right">42.90</td>
    <td align="right">92.64</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.04</td>
    <td align="right">24.43</td>
    <td align="right">21.51</td>
    <td align="right">27.56</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.23</td>
    <td align="right">25.12</td>
    <td align="right">24.91</td>
    <td align="right">30.03</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">12.58</td>
    <td align="right">17.18</td>
    <td align="right">15.78</td>
    <td align="right">23.58</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.29</td>
    <td align="right">5.56</td>
    <td align="right">5.85</td>
    <td align="right">12.19</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.37</td>
    <td align="right">6.30</td>
    <td align="right">6.80</td>
    <td align="right">12.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.30</td>
    <td align="right">57.43</td>
    <td align="right">43.57</td>
    <td align="right">58.54</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.96</td>
    <td align="right">11.86</td>
    <td align="right">11.21</td>
    <td align="right">17.16</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.66</td>
    <td align="right">12.86</td>
    <td align="right">12.77</td>
    <td align="right">19.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">79.44</td>
    <td align="right">110.17</td>
    <td align="right">73.28</td>
    <td align="right">106.91</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.83</td>
    <td align="right">17.98</td>
    <td align="right">17.79</td>
    <td align="right">23.10</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.56</td>
    <td align="right">20.43</td>
    <td align="right">18.38</td>
    <td align="right">24.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">117.02</td>
    <td align="right">162.69</td>
    <td align="right">121.10</td>
    <td align="right">174.30</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.65</td>
    <td align="right">24.37</td>
    <td align="right">21.52</td>
    <td align="right">27.52</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.23</td>
    <td align="right">25.11</td>
    <td align="right">24.88</td>
    <td align="right">29.99</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.19</td>
    <td align="right">7.34</td>
    <td align="right">16.10</td>
    <td align="right">14.37</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.02</td>
    <td align="right">9.02</td>
    <td align="right">16.55</td>
    <td align="right">15.27</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.55</td>
    <td align="right">5.18</td>
    <td align="right">5.54</td>
    <td align="right">14.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">14.52</td>
    <td align="right">16.17</td>
    <td align="right">20.15</td>
    <td align="right">20.57</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.86</td>
    <td align="right">19.62</td>
    <td align="right">23.99</td>
    <td align="right">23.61</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.63</td>
    <td align="right">8.70</td>
    <td align="right">8.54</td>
    <td align="right">15.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">28.67</td>
    <td align="right">29.55</td>
    <td align="right">23.93</td>
    <td align="right">30.17</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.63</td>
    <td align="right">31.02</td>
    <td align="right">26.02</td>
    <td align="right">32.44</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.35</td>
    <td align="right">20.60</td>
    <td align="right">14.49</td>
    <td align="right">24.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.13</td>
    <td align="right">38.87</td>
    <td align="right">24.95</td>
    <td align="right">39.01</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.25</td>
    <td align="right">42.47</td>
    <td align="right">31.34</td>
    <td align="right">44.39</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.48</td>
    <td align="right">23.79</td>
    <td align="right">16.28</td>
    <td align="right">28.45</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">5.98</td>
    <td align="right">7.34</td>
    <td align="right">7.42</td>
    <td align="right">14.18</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.65</td>
    <td align="right">9.68</td>
    <td align="right">9.69</td>
    <td align="right">16.42</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.77</td>
    <td align="right">4.23</td>
    <td align="right">4.71</td>
    <td align="right">13.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.64</td>
    <td align="right">15.37</td>
    <td align="right">15.26</td>
    <td align="right">21.27</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.53</td>
    <td align="right">19.67</td>
    <td align="right">18.65</td>
    <td align="right">25.61</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.45</td>
    <td align="right">8.51</td>
    <td align="right">8.34</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">28.46</td>
    <td align="right">30.62</td>
    <td align="right">30.28</td>
    <td align="right">35.47</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.12</td>
    <td align="right">32.24</td>
    <td align="right">32.09</td>
    <td align="right">37.75</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.45</td>
    <td align="right">20.45</td>
    <td align="right">18.76</td>
    <td align="right">26.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.19</td>
    <td align="right">38.64</td>
    <td align="right">38.47</td>
    <td align="right">43.52</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.95</td>
    <td align="right">49.84</td>
    <td align="right">49.39</td>
    <td align="right">55.54</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.48</td>
    <td align="right">23.44</td>
    <td align="right">21.15</td>
    <td align="right">29.64</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.29</td>
    <td align="right">4.79</td>
    <td align="right">5.04</td>
    <td align="right">14.53</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.55</td>
    <td align="right">5.69</td>
    <td align="right">6.06</td>
    <td align="right">16.09</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.75</td>
    <td align="right">5.61</td>
    <td align="right">5.92</td>
    <td align="right">15.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.28</td>
    <td align="right">9.57</td>
    <td align="right">9.05</td>
    <td align="right">16.31</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.25</td>
    <td align="right">10.30</td>
    <td align="right">10.05</td>
    <td align="right">18.30</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.38</td>
    <td align="right">12.67</td>
    <td align="right">12.23</td>
    <td align="right">19.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.65</td>
    <td align="right">20.76</td>
    <td align="right">14.47</td>
    <td align="right">24.60</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.31</td>
    <td align="right">25.94</td>
    <td align="right">19.71</td>
    <td align="right">29.88</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.07</td>
    <td align="right">26.78</td>
    <td align="right">19.95</td>
    <td align="right">29.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.56</td>
    <td align="right">23.65</td>
    <td align="right">16.06</td>
    <td align="right">27.74</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.22</td>
    <td align="right">35.58</td>
    <td align="right">22.69</td>
    <td align="right">36.48</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.69</td>
    <td align="right">31.80</td>
    <td align="right">22.72</td>
    <td align="right">35.77</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.89</td>
    <td align="right">4.27</td>
    <td align="right">4.68</td>
    <td align="right">13.27</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.86</td>
    <td align="right">6.08</td>
    <td align="right">6.37</td>
    <td align="right">16.25</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.15</td>
    <td align="right">6.09</td>
    <td align="right">6.35</td>
    <td align="right">15.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.94</td>
    <td align="right">9.16</td>
    <td align="right">8.74</td>
    <td align="right">15.85</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.57</td>
    <td align="right">10.75</td>
    <td align="right">10.51</td>
    <td align="right">18.37</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.67</td>
    <td align="right">11.83</td>
    <td align="right">11.35</td>
    <td align="right">18.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.19</td>
    <td align="right">20.20</td>
    <td align="right">18.26</td>
    <td align="right">24.98</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.25</td>
    <td align="right">25.76</td>
    <td align="right">25.34</td>
    <td align="right">31.69</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.59</td>
    <td align="right">25.73</td>
    <td align="right">25.27</td>
    <td align="right">31.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.63</td>
    <td align="right">23.52</td>
    <td align="right">21.11</td>
    <td align="right">28.71</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.38</td>
    <td align="right">31.68</td>
    <td align="right">31.58</td>
    <td align="right">37.04</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.82</td>
    <td align="right">31.77</td>
    <td align="right">31.65</td>
    <td align="right">36.78</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.30</td>
    <td align="right">9.14</td>
    <td align="right">16.35</td>
    <td align="right">15.12</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.48</td>
    <td align="right">10.49</td>
    <td align="right">21.91</td>
    <td align="right">18.32</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.91</td>
    <td align="right">15.46</td>
    <td align="right">22.97</td>
    <td align="right">21.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.34</td>
    <td align="right">18.03</td>
    <td align="right">18.91</td>
    <td align="right">22.71</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.80</td>
    <td align="right">21.06</td>
    <td align="right">21.72</td>
    <td align="right">25.64</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.36</td>
    <td align="right">30.40</td>
    <td align="right">25.00</td>
    <td align="right">31.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.68</td>
    <td align="right">27.63</td>
    <td align="right">21.56</td>
    <td align="right">30.77</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.39</td>
    <td align="right">33.33</td>
    <td align="right">26.17</td>
    <td align="right">37.09</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">47.06</td>
    <td align="right">46.84</td>
    <td align="right">24.82</td>
    <td align="right">40.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.29</td>
    <td align="right">42.54</td>
    <td align="right">25.29</td>
    <td align="right">42.81</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.02</td>
    <td align="right">50.25</td>
    <td align="right">28.31</td>
    <td align="right">48.32</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">75.15</td>
    <td align="right">66.18</td>
    <td align="right">27.27</td>
    <td align="right">55.97</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.21</td>
    <td align="right">9.13</td>
    <td align="right">9.25</td>
    <td align="right">15.92</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">11.96</td>
    <td align="right">10.00</td>
    <td align="right">10.12</td>
    <td align="right">17.99</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.84</td>
    <td align="right">13.75</td>
    <td align="right">13.97</td>
    <td align="right">20.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.70</td>
    <td align="right">17.52</td>
    <td align="right">17.41</td>
    <td align="right">23.61</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.86</td>
    <td align="right">21.70</td>
    <td align="right">21.61</td>
    <td align="right">27.89</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.66</td>
    <td align="right">30.29</td>
    <td align="right">30.16</td>
    <td align="right">36.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.81</td>
    <td align="right">31.04</td>
    <td align="right">30.91</td>
    <td align="right">36.75</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.30</td>
    <td align="right">40.37</td>
    <td align="right">39.60</td>
    <td align="right">45.86</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.69</td>
    <td align="right">50.12</td>
    <td align="right">49.22</td>
    <td align="right">54.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.35</td>
    <td align="right">43.13</td>
    <td align="right">43.03</td>
    <td align="right">47.99</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.95</td>
    <td align="right">51.33</td>
    <td align="right">51.36</td>
    <td align="right">56.30</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.48</td>
    <td align="right">74.57</td>
    <td align="right">74.10</td>
    <td align="right">79.43</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.11</td>
    <td align="right">6.13</td>
    <td align="right">3.91</td>
    <td align="right">12.85</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.39</td>
    <td align="right">11.17</td>
    <td align="right">18.40</td>
    <td align="right">15.86</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.50</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">4.85</td>
    <td align="right">4.84</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.25</td>
    <td align="right">15.87</td>
    <td align="right">19.50</td>
    <td align="right">19.41</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.02</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.46</td>
    <td align="right">5.41</td>
    <td align="right">5.41</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.85</td>
    <td align="right">19.35</td>
    <td align="right">18.85</td>
    <td align="right">21.78</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.42</td>
    <td align="right">5.71</td>
    <td align="right">5.70</td>
    <td align="right">5.71</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.90</td>
    <td align="right">5.83</td>
    <td align="right">5.83</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.73</td>
    <td align="right">23.29</td>
    <td align="right">19.19</td>
    <td align="right">24.23</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.84</td>
    <td align="right">6.26</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.22</td>
    <td align="right">3.63</td>
    <td align="right">3.63</td>
    <td align="right">3.63</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.45</td>
    <td align="right">10.47</td>
    <td align="right">10.50</td>
    <td align="right">10.59</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.50</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">4.84</td>
    <td align="right">4.84</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.41</td>
    <td align="right">14.51</td>
    <td align="right">14.46</td>
    <td align="right">14.43</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.02</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.48</td>
    <td align="right">5.43</td>
    <td align="right">5.43</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.78</td>
    <td align="right">16.93</td>
    <td align="right">16.95</td>
    <td align="right">16.98</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.41</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.90</td>
    <td align="right">5.83</td>
    <td align="right">5.84</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.86</td>
    <td align="right">24.71</td>
    <td align="right">24.64</td>
    <td align="right">24.69</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.82</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.24</td>
    <td align="right">3.64</td>
    <td align="right">3.63</td>
    <td align="right">3.63</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.13</td>
    <td align="right">6.31</td>
    <td align="right">14.71</td>
    <td align="right">11.90</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.22</td>
    <td align="right">6.13</td>
    <td align="right">13.94</td>
    <td align="right">11.66</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.61</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.94</td>
    <td align="right">8.76</td>
    <td align="right">14.24</td>
    <td align="right">14.09</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.89</td>
    <td align="right">8.73</td>
    <td align="right">14.53</td>
    <td align="right">14.23</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.26</td>
    <td align="right">3.24</td>
    <td align="right">3.23</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.34</td>
    <td align="right">11.95</td>
    <td align="right">16.05</td>
    <td align="right">16.45</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.56</td>
    <td align="right">11.70</td>
    <td align="right">15.95</td>
    <td align="right">16.30</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.21</td>
    <td align="right">4.16</td>
    <td align="right">2.71</td>
    <td align="right">13.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.70</td>
    <td align="right">13.39</td>
    <td align="right">14.98</td>
    <td align="right">17.70</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.77</td>
    <td align="right">13.68</td>
    <td align="right">15.38</td>
    <td align="right">18.24</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.28</td>
    <td align="right">4.17</td>
    <td align="right">2.68</td>
    <td align="right">13.36</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.13</td>
    <td align="right">6.23</td>
    <td align="right">6.22</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.18</td>
    <td align="right">6.10</td>
    <td align="right">6.09</td>
    <td align="right">6.09</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.61</td>
    <td align="right">3.34</td>
    <td align="right">3.35</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.93</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.86</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.23</td>
    <td align="right">3.24</td>
    <td align="right">3.24</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.34</td>
    <td align="right">7.75</td>
    <td align="right">7.75</td>
    <td align="right">7.76</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.57</td>
    <td align="right">7.62</td>
    <td align="right">7.60</td>
    <td align="right">7.65</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.21</td>
    <td align="right">4.82</td>
    <td align="right">4.81</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.85</td>
    <td align="right">8.36</td>
    <td align="right">8.36</td>
    <td align="right">8.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.79</td>
    <td align="right">8.59</td>
    <td align="right">8.55</td>
    <td align="right">8.58</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.25</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.86</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.65</td>
    <td align="right">3.04</td>
    <td align="right">3.03</td>
    <td align="right">3.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.68</td>
    <td align="right">4.25</td>
    <td align="right">4.26</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.89</td>
    <td align="right">4.03</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.77</td>
    <td align="right">3.11</td>
    <td align="right">3.10</td>
    <td align="right">3.11</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.14</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.09</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.42</td>
    <td align="right">4.19</td>
    <td align="right">2.58</td>
    <td align="right">13.26</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.46</td>
    <td align="right">5.69</td>
    <td align="right">3.82</td>
    <td align="right">16.31</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.90</td>
    <td align="right">5.54</td>
    <td align="right">3.69</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.49</td>
    <td align="right">4.21</td>
    <td align="right">2.56</td>
    <td align="right">13.16</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.70</td>
    <td align="right">6.95</td>
    <td align="right">3.77</td>
    <td align="right">16.83</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.05</td>
    <td align="right">6.40</td>
    <td align="right">3.68</td>
    <td align="right">16.53</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.64</td>
    <td align="right">3.04</td>
    <td align="right">3.03</td>
    <td align="right">3.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.65</td>
    <td align="right">4.26</td>
    <td align="right">4.26</td>
    <td align="right">4.26</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.89</td>
    <td align="right">4.04</td>
    <td align="right">4.05</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.73</td>
    <td align="right">3.11</td>
    <td align="right">3.10</td>
    <td align="right">3.11</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.16</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.07</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.42</td>
    <td align="right">4.48</td>
    <td align="right">4.47</td>
    <td align="right">4.48</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.46</td>
    <td align="right">6.23</td>
    <td align="right">6.08</td>
    <td align="right">6.22</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.82</td>
    <td align="right">6.11</td>
    <td align="right">6.09</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.45</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.70</td>
    <td align="right">7.50</td>
    <td align="right">7.23</td>
    <td align="right">7.50</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.14</td>
    <td align="right">7.37</td>
    <td align="right">7.01</td>
    <td align="right">7.36</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">5.98</td>
    <td align="right">7.50</td>
    <td align="right">14.11</td>
    <td align="right">12.93</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">7.81</td>
    <td align="right">17.55</td>
    <td align="right">14.98</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.38</td>
    <td align="right">10.41</td>
    <td align="right">18.38</td>
    <td align="right">15.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.04</td>
    <td align="right">10.06</td>
    <td align="right">14.21</td>
    <td align="right">15.36</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.75</td>
    <td align="right">10.04</td>
    <td align="right">14.84</td>
    <td align="right">16.32</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.59</td>
    <td align="right">13.97</td>
    <td align="right">19.20</td>
    <td align="right">18.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.03</td>
    <td align="right">11.65</td>
    <td align="right">13.87</td>
    <td align="right">16.53</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.66</td>
    <td align="right">12.40</td>
    <td align="right">15.82</td>
    <td align="right">18.57</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.69</td>
    <td align="right">14.30</td>
    <td align="right">16.67</td>
    <td align="right">19.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.33</td>
    <td align="right">13.92</td>
    <td align="right">14.37</td>
    <td align="right">18.46</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.77</td>
    <td align="right">13.41</td>
    <td align="right">15.62</td>
    <td align="right">19.31</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.75</td>
    <td align="right">21.22</td>
    <td align="right">20.07</td>
    <td align="right">23.40</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">5.99</td>
    <td align="right">7.55</td>
    <td align="right">7.54</td>
    <td align="right">7.54</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.72</td>
    <td align="right">8.78</td>
    <td align="right">8.78</td>
    <td align="right">8.78</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.20</td>
    <td align="right">11.13</td>
    <td align="right">10.74</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.06</td>
    <td align="right">10.27</td>
    <td align="right">10.30</td>
    <td align="right">10.29</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">14.71</td>
    <td align="right">10.56</td>
    <td align="right">10.56</td>
    <td align="right">10.55</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.45</td>
    <td align="right">14.99</td>
    <td align="right">14.99</td>
    <td align="right">14.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.06</td>
    <td align="right">11.92</td>
    <td align="right">11.91</td>
    <td align="right">11.93</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.47</td>
    <td align="right">13.44</td>
    <td align="right">13.42</td>
    <td align="right">13.40</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">14.64</td>
    <td align="right">16.13</td>
    <td align="right">17.01</td>
    <td align="right">16.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.34</td>
    <td align="right">14.46</td>
    <td align="right">14.46</td>
    <td align="right">14.47</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.14</td>
    <td align="right">15.50</td>
    <td align="right">15.49</td>
    <td align="right">15.49</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.68</td>
    <td align="right">20.45</td>
    <td align="right">20.57</td>
    <td align="right">22.59</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.01</td>
    <td align="right">23.62</td>
    <td align="right">13.51</td>
    <td align="right">30.55</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.45</td>
    <td align="right">15.07</td>
    <td align="right">21.27</td>
    <td align="right">18.87</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.28</td>
    <td align="right">6.52</td>
    <td align="right">6.44</td>
    <td align="right">6.50</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.72</td>
    <td align="right">6.57</td>
    <td align="right">6.59</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.84</td>
    <td align="right">54.76</td>
    <td align="right">27.78</td>
    <td align="right">41.37</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.56</td>
    <td align="right">12.10</td>
    <td align="right">12.12</td>
    <td align="right">12.11</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">10.76</td>
    <td align="right">11.95</td>
    <td align="right">11.98</td>
    <td align="right">12.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.90</td>
    <td align="right">85.35</td>
    <td align="right">31.70</td>
    <td align="right">59.74</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.46</td>
    <td align="right">18.51</td>
    <td align="right">18.52</td>
    <td align="right">18.57</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.36</td>
    <td align="right">20.60</td>
    <td align="right">20.59</td>
    <td align="right">20.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.61</td>
    <td align="right">127.00</td>
    <td align="right">38.48</td>
    <td align="right">85.57</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.45</td>
    <td align="right">24.96</td>
    <td align="right">24.95</td>
    <td align="right">25.01</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.23</td>
    <td align="right">16.34</td>
    <td align="right">16.34</td>
    <td align="right">16.33</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.36</td>
    <td align="right">14.36</td>
    <td align="right">14.37</td>
    <td align="right">14.36</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.35</td>
    <td align="right">6.60</td>
    <td align="right">6.63</td>
    <td align="right">6.61</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.70</td>
    <td align="right">6.58</td>
    <td align="right">6.56</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">43.12</td>
    <td align="right">36.54</td>
    <td align="right">36.52</td>
    <td align="right">36.53</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.14</td>
    <td align="right">12.75</td>
    <td align="right">12.66</td>
    <td align="right">12.73</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.63</td>
    <td align="right">12.86</td>
    <td align="right">12.81</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.26</td>
    <td align="right">71.80</td>
    <td align="right">71.82</td>
    <td align="right">71.81</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.57</td>
    <td align="right">18.61</td>
    <td align="right">18.62</td>
    <td align="right">18.61</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.32</td>
    <td align="right">20.55</td>
    <td align="right">20.57</td>
    <td align="right">20.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.65</td>
    <td align="right">109.90</td>
    <td align="right">109.89</td>
    <td align="right">109.91</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.42</td>
    <td align="right">24.90</td>
    <td align="right">24.93</td>
    <td align="right">24.94</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.18</td>
    <td align="right">16.29</td>
    <td align="right">16.28</td>
    <td align="right">16.28</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">3.80</td>
    <td align="right">7.41</td>
    <td align="right">14.79</td>
    <td align="right">13.60</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">3.84</td>
    <td align="right">7.44</td>
    <td align="right">14.56</td>
    <td align="right">13.51</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.57</td>
    <td align="right">4.63</td>
    <td align="right">4.56</td>
    <td align="right">4.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.05</td>
    <td align="right">15.94</td>
    <td align="right">18.27</td>
    <td align="right">20.32</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.95</td>
    <td align="right">17.68</td>
    <td align="right">18.39</td>
    <td align="right">20.65</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.99</td>
    <td align="right">8.91</td>
    <td align="right">8.87</td>
    <td align="right">8.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.12</td>
    <td align="right">29.44</td>
    <td align="right">23.29</td>
    <td align="right">29.54</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.99</td>
    <td align="right">30.05</td>
    <td align="right">22.10</td>
    <td align="right">29.90</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.81</td>
    <td align="right">15.85</td>
    <td align="right">10.27</td>
    <td align="right">20.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.36</td>
    <td align="right">39.82</td>
    <td align="right">24.69</td>
    <td align="right">38.78</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.59</td>
    <td align="right">41.16</td>
    <td align="right">25.49</td>
    <td align="right">40.43</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.09</td>
    <td align="right">18.39</td>
    <td align="right">12.21</td>
    <td align="right">23.14</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.24</td>
    <td align="right">7.96</td>
    <td align="right">7.99</td>
    <td align="right">7.95</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.37</td>
    <td align="right">8.05</td>
    <td align="right">8.03</td>
    <td align="right">8.01</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.36</td>
    <td align="right">4.36</td>
    <td align="right">4.33</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">7.98</td>
    <td align="right">11.07</td>
    <td align="right">11.05</td>
    <td align="right">11.11</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.84</td>
    <td align="right">12.22</td>
    <td align="right">12.22</td>
    <td align="right">12.25</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.97</td>
    <td align="right">8.88</td>
    <td align="right">8.88</td>
    <td align="right">8.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.24</td>
    <td align="right">23.22</td>
    <td align="right">23.24</td>
    <td align="right">23.24</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.12</td>
    <td align="right">24.65</td>
    <td align="right">24.66</td>
    <td align="right">24.66</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.76</td>
    <td align="right">16.50</td>
    <td align="right">16.48</td>
    <td align="right">16.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.40</td>
    <td align="right">30.00</td>
    <td align="right">30.01</td>
    <td align="right">30.02</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.54</td>
    <td align="right">31.09</td>
    <td align="right">31.10</td>
    <td align="right">31.11</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.06</td>
    <td align="right">18.66</td>
    <td align="right">18.64</td>
    <td align="right">18.63</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.66</td>
    <td align="right">4.47</td>
    <td align="right">4.39</td>
    <td align="right">4.44</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.33</td>
    <td align="right">7.40</td>
    <td align="right">7.41</td>
    <td align="right">7.41</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.46</td>
    <td align="right">5.97</td>
    <td align="right">6.01</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.26</td>
    <td align="right">9.35</td>
    <td align="right">9.33</td>
    <td align="right">9.32</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.29</td>
    <td align="right">9.82</td>
    <td align="right">9.81</td>
    <td align="right">9.88</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.89</td>
    <td align="right">11.38</td>
    <td align="right">11.37</td>
    <td align="right">11.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.11</td>
    <td align="right">16.19</td>
    <td align="right">10.23</td>
    <td align="right">20.45</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.53</td>
    <td align="right">20.57</td>
    <td align="right">14.43</td>
    <td align="right">27.06</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.09</td>
    <td align="right">19.51</td>
    <td align="right">14.57</td>
    <td align="right">25.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.54</td>
    <td align="right">18.43</td>
    <td align="right">11.31</td>
    <td align="right">22.68</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.11</td>
    <td align="right">26.97</td>
    <td align="right">16.03</td>
    <td align="right">30.70</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.01</td>
    <td align="right">27.17</td>
    <td align="right">16.28</td>
    <td align="right">30.07</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.26</td>
    <td align="right">3.99</td>
    <td align="right">3.95</td>
    <td align="right">3.94</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.35</td>
    <td align="right">6.35</td>
    <td align="right">6.33</td>
    <td align="right">6.30</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.73</td>
    <td align="right">4.98</td>
    <td align="right">4.99</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.00</td>
    <td align="right">9.02</td>
    <td align="right">9.04</td>
    <td align="right">9.02</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.61</td>
    <td align="right">10.22</td>
    <td align="right">10.22</td>
    <td align="right">10.25</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.86</td>
    <td align="right">11.37</td>
    <td align="right">11.39</td>
    <td align="right">11.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.08</td>
    <td align="right">16.29</td>
    <td align="right">16.28</td>
    <td align="right">16.32</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.25</td>
    <td align="right">21.18</td>
    <td align="right">21.18</td>
    <td align="right">21.17</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.72</td>
    <td align="right">21.38</td>
    <td align="right">21.37</td>
    <td align="right">21.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.45</td>
    <td align="right">18.50</td>
    <td align="right">18.50</td>
    <td align="right">18.51</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.13</td>
    <td align="right">30.27</td>
    <td align="right">30.25</td>
    <td align="right">30.23</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.05</td>
    <td align="right">30.25</td>
    <td align="right">30.23</td>
    <td align="right">30.25</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.87</td>
    <td align="right">9.53</td>
    <td align="right">15.67</td>
    <td align="right">15.50</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.27</td>
    <td align="right">10.42</td>
    <td align="right">19.19</td>
    <td align="right">17.73</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.52</td>
    <td align="right">14.94</td>
    <td align="right">20.45</td>
    <td align="right">18.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.74</td>
    <td align="right">18.07</td>
    <td align="right">18.01</td>
    <td align="right">22.30</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.70</td>
    <td align="right">19.83</td>
    <td align="right">18.20</td>
    <td align="right">23.70</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">33.65</td>
    <td align="right">30.64</td>
    <td align="right">24.07</td>
    <td align="right">29.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.01</td>
    <td align="right">27.52</td>
    <td align="right">21.91</td>
    <td align="right">30.25</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.94</td>
    <td align="right">32.78</td>
    <td align="right">23.88</td>
    <td align="right">35.77</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">49.79</td>
    <td align="right">44.78</td>
    <td align="right">23.09</td>
    <td align="right">39.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.44</td>
    <td align="right">41.31</td>
    <td align="right">24.68</td>
    <td align="right">42.28</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.18</td>
    <td align="right">39.57</td>
    <td align="right">26.37</td>
    <td align="right">42.34</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.04</td>
    <td align="right">71.19</td>
    <td align="right">30.41</td>
    <td align="right">57.70</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.52</td>
    <td align="right">9.30</td>
    <td align="right">9.31</td>
    <td align="right">9.34</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.23</td>
    <td align="right">10.55</td>
    <td align="right">10.54</td>
    <td align="right">10.51</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.61</td>
    <td align="right">13.90</td>
    <td align="right">13.96</td>
    <td align="right">13.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.87</td>
    <td align="right">17.74</td>
    <td align="right">17.81</td>
    <td align="right">17.77</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">24.05</td>
    <td align="right">22.37</td>
    <td align="right">22.33</td>
    <td align="right">22.37</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.31</td>
    <td align="right">31.93</td>
    <td align="right">31.92</td>
    <td align="right">31.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.06</td>
    <td align="right">31.68</td>
    <td align="right">31.65</td>
    <td align="right">31.63</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.47</td>
    <td align="right">39.67</td>
    <td align="right">39.62</td>
    <td align="right">39.59</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.25</td>
    <td align="right">52.12</td>
    <td align="right">52.10</td>
    <td align="right">52.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.54</td>
    <td align="right">43.06</td>
    <td align="right">43.00</td>
    <td align="right">43.02</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.55</td>
    <td align="right">51.06</td>
    <td align="right">51.07</td>
    <td align="right">51.09</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.91</td>
    <td align="right">76.00</td>
    <td align="right">75.94</td>
    <td align="right">76.19</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.95</td>
    <td align="right">2.67</td>
    <td align="right">1.90</td>
    <td align="right">9.16</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">5.50</td>
    <td align="right">3.80</td>
    <td align="right">11.62</td>
    <td align="right">8.40</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.17</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.30</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.34</td>
    <td align="right">5.53</td>
    <td align="right">12.11</td>
    <td align="right">9.89</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.32</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.45</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.51</td>
    <td align="right">6.64</td>
    <td align="right">11.48</td>
    <td align="right">10.72</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.53</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.62</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.50</td>
    <td align="right">8.50</td>
    <td align="right">11.64</td>
    <td align="right">11.85</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.62</td>
    <td align="right">1.61</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">5.53</td>
    <td align="right">3.54</td>
    <td align="right">3.55</td>
    <td align="right">3.56</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.18</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.30</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.34</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.33</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.45</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.52</td>
    <td align="right">6.57</td>
    <td align="right">6.55</td>
    <td align="right">6.55</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.54</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.64</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.55</td>
    <td align="right">8.51</td>
    <td align="right">8.52</td>
    <td align="right">8.50</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.62</td>
    <td align="right">1.60</td>
    <td align="right">1.61</td>
    <td align="right">1.60</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.91</td>
    <td align="right">2.68</td>
    <td align="right">9.42</td>
    <td align="right">7.36</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.99</td>
    <td align="right">2.77</td>
    <td align="right">8.99</td>
    <td align="right">7.13</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.62</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.07</td>
    <td align="right">4.04</td>
    <td align="right">10.61</td>
    <td align="right">8.76</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.52</td>
    <td align="right">3.71</td>
    <td align="right">9.78</td>
    <td align="right">7.96</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.40</td>
    <td align="right">1.50</td>
    <td align="right">1.51</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.53</td>
    <td align="right">4.96</td>
    <td align="right">10.60</td>
    <td align="right">9.33</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">4.95</td>
    <td align="right">10.12</td>
    <td align="right">9.02</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.66</td>
    <td align="right">2.48</td>
    <td align="right">1.56</td>
    <td align="right">11.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.11</td>
    <td align="right">5.65</td>
    <td align="right">10.22</td>
    <td align="right">9.78</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.30</td>
    <td align="right">5.96</td>
    <td align="right">10.39</td>
    <td align="right">9.67</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.77</td>
    <td align="right">2.96</td>
    <td align="right">1.53</td>
    <td align="right">11.34</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.93</td>
    <td align="right">1.74</td>
    <td align="right">1.72</td>
    <td align="right">1.71</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">1.79</td>
    <td align="right">1.81</td>
    <td align="right">1.80</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.61</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.51</td>
    <td align="right">2.23</td>
    <td align="right">2.22</td>
    <td align="right">2.22</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.41</td>
    <td align="right">1.51</td>
    <td align="right">1.51</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.50</td>
    <td align="right">2.70</td>
    <td align="right">2.69</td>
    <td align="right">2.71</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.51</td>
    <td align="right">2.83</td>
    <td align="right">2.82</td>
    <td align="right">2.82</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.67</td>
    <td align="right">2.45</td>
    <td align="right">2.43</td>
    <td align="right">2.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.12</td>
    <td align="right">3.12</td>
    <td align="right">3.11</td>
    <td align="right">3.14</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.43</td>
    <td align="right">3.33</td>
    <td align="right">3.37</td>
    <td align="right">3.37</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.70</td>
    <td align="right">2.98</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.66</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.93</td>
    <td align="right">2.72</td>
    <td align="right">9.45</td>
    <td align="right">7.39</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.98</td>
    <td align="right">2.78</td>
    <td align="right">9.02</td>
    <td align="right">7.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.69</td>
    <td align="right">1.55</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.10</td>
    <td align="right">4.08</td>
    <td align="right">10.67</td>
    <td align="right">8.83</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.54</td>
    <td align="right">3.73</td>
    <td align="right">9.81</td>
    <td align="right">8.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.70</td>
    <td align="right">2.52</td>
    <td align="right">1.59</td>
    <td align="right">11.39</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.56</td>
    <td align="right">4.98</td>
    <td align="right">10.63</td>
    <td align="right">9.37</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">4.96</td>
    <td align="right">10.08</td>
    <td align="right">8.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.67</td>
    <td align="right">2.90</td>
    <td align="right">1.52</td>
    <td align="right">11.30</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.11</td>
    <td align="right">5.64</td>
    <td align="right">10.20</td>
    <td align="right">9.71</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.46</td>
    <td align="right">6.03</td>
    <td align="right">10.42</td>
    <td align="right">9.70</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.63</td>
    <td align="right">1.71</td>
    <td align="right">1.72</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.92</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.96</td>
    <td align="right">1.79</td>
    <td align="right">1.79</td>
    <td align="right">1.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.67</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.53</td>
    <td align="right">2.23</td>
    <td align="right">2.24</td>
    <td align="right">2.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.68</td>
    <td align="right">2.45</td>
    <td align="right">2.45</td>
    <td align="right">2.45</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.52</td>
    <td align="right">2.70</td>
    <td align="right">2.70</td>
    <td align="right">2.69</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">2.85</td>
    <td align="right">2.84</td>
    <td align="right">2.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.67</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.13</td>
    <td align="right">3.11</td>
    <td align="right">3.11</td>
    <td align="right">3.19</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.33</td>
    <td align="right">3.38</td>
    <td align="right">3.39</td>
    <td align="right">3.35</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.19</td>
    <td align="right">3.44</td>
    <td align="right">10.11</td>
    <td align="right">8.34</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.83</td>
    <td align="right">3.78</td>
    <td align="right">12.60</td>
    <td align="right">9.28</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.61</td>
    <td align="right">5.19</td>
    <td align="right">13.33</td>
    <td align="right">9.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.35</td>
    <td align="right">4.58</td>
    <td align="right">9.73</td>
    <td align="right">9.54</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.23</td>
    <td align="right">4.63</td>
    <td align="right">10.10</td>
    <td align="right">10.08</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.61</td>
    <td align="right">7.00</td>
    <td align="right">13.50</td>
    <td align="right">11.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.43</td>
    <td align="right">5.41</td>
    <td align="right">9.62</td>
    <td align="right">10.17</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.47</td>
    <td align="right">5.91</td>
    <td align="right">11.18</td>
    <td align="right">11.14</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.71</td>
    <td align="right">7.76</td>
    <td align="right">11.95</td>
    <td align="right">11.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.04</td>
    <td align="right">6.55</td>
    <td align="right">10.29</td>
    <td align="right">10.94</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.42</td>
    <td align="right">6.46</td>
    <td align="right">10.83</td>
    <td align="right">11.71</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.05</td>
    <td align="right">11.14</td>
    <td align="right">13.36</td>
    <td align="right">13.48</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.18</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.85</td>
    <td align="right">3.82</td>
    <td align="right">3.79</td>
    <td align="right">3.79</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.63</td>
    <td align="right">4.91</td>
    <td align="right">4.91</td>
    <td align="right">4.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.35</td>
    <td align="right">3.97</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.60</td>
    <td align="right">4.28</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.63</td>
    <td align="right">6.68</td>
    <td align="right">6.67</td>
    <td align="right">6.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.47</td>
    <td align="right">4.76</td>
    <td align="right">4.76</td>
    <td align="right">4.76</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.46</td>
    <td align="right">5.40</td>
    <td align="right">5.40</td>
    <td align="right">5.40</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.68</td>
    <td align="right">7.59</td>
    <td align="right">7.56</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.97</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
    <td align="right">5.96</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.50</td>
    <td align="right">6.21</td>
    <td align="right">6.19</td>
    <td align="right">6.22</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.00</td>
    <td align="right">10.99</td>
    <td align="right">10.99</td>
    <td align="right">11.02</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.48</td>
    <td align="right">11.51</td>
    <td align="right">5.75</td>
    <td align="right">15.39</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">6.64</td>
    <td align="right">5.52</td>
    <td align="right">13.14</td>
    <td align="right">9.85</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.87</td>
    <td align="right">2.16</td>
    <td align="right">2.19</td>
    <td align="right">2.17</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.86</td>
    <td align="right">2.10</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">11.89</td>
    <td align="right">10.86</td>
    <td align="right">16.43</td>
    <td align="right">14.24</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.29</td>
    <td align="right">4.27</td>
    <td align="right">4.10</td>
    <td align="right">3.88</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.31</td>
    <td align="right">3.83</td>
    <td align="right">3.78</td>
    <td align="right">3.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">27.94</td>
    <td align="right">22.76</td>
    <td align="right">18.92</td>
    <td align="right">20.60</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.13</td>
    <td align="right">7.33</td>
    <td align="right">7.16</td>
    <td align="right">6.86</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.82</td>
    <td align="right">6.80</td>
    <td align="right">6.62</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">46.80</td>
    <td align="right">36.70</td>
    <td align="right">21.81</td>
    <td align="right">29.14</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.51</td>
    <td align="right">8.35</td>
    <td align="right">8.59</td>
    <td align="right">9.13</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.68</td>
    <td align="right">7.37</td>
    <td align="right">7.20</td>
    <td align="right">7.28</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">6.64</td>
    <td align="right">5.68</td>
    <td align="right">5.67</td>
    <td align="right">5.68</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.88</td>
    <td align="right">2.19</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.87</td>
    <td align="right">2.08</td>
    <td align="right">2.09</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">11.82</td>
    <td align="right">12.20</td>
    <td align="right">11.36</td>
    <td align="right">11.63</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.68</td>
    <td align="right">4.36</td>
    <td align="right">3.95</td>
    <td align="right">3.88</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.48</td>
    <td align="right">3.85</td>
    <td align="right">3.95</td>
    <td align="right">3.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">27.85</td>
    <td align="right">26.22</td>
    <td align="right">25.75</td>
    <td align="right">23.76</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.94</td>
    <td align="right">6.32</td>
    <td align="right">6.73</td>
    <td align="right">6.70</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.84</td>
    <td align="right">7.00</td>
    <td align="right">7.16</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">49.57</td>
    <td align="right">42.68</td>
    <td align="right">42.75</td>
    <td align="right">40.51</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.97</td>
    <td align="right">8.89</td>
    <td align="right">9.23</td>
    <td align="right">9.06</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.20</td>
    <td align="right">6.58</td>
    <td align="right">7.12</td>
    <td align="right">7.46</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.29</td>
    <td align="right">3.55</td>
    <td align="right">10.23</td>
    <td align="right">8.40</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.37</td>
    <td align="right">3.64</td>
    <td align="right">9.82</td>
    <td align="right">8.27</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.99</td>
    <td align="right">2.55</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.52</td>
    <td align="right">7.32</td>
    <td align="right">13.48</td>
    <td align="right">13.36</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.54</td>
    <td align="right">7.27</td>
    <td align="right">12.66</td>
    <td align="right">11.45</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.93</td>
    <td align="right">3.94</td>
    <td align="right">3.86</td>
    <td align="right">3.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.89</td>
    <td align="right">13.97</td>
    <td align="right">15.86</td>
    <td align="right">16.65</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.12</td>
    <td align="right">14.29</td>
    <td align="right">15.09</td>
    <td align="right">16.87</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.54</td>
    <td align="right">8.68</td>
    <td align="right">5.66</td>
    <td align="right">15.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.58</td>
    <td align="right">18.34</td>
    <td align="right">15.82</td>
    <td align="right">20.82</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">16.02</td>
    <td align="right">20.79</td>
    <td align="right">16.02</td>
    <td align="right">20.38</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.39</td>
    <td align="right">10.69</td>
    <td align="right">6.29</td>
    <td align="right">16.13</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.26</td>
    <td align="right">2.53</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.34</td>
    <td align="right">2.58</td>
    <td align="right">2.60</td>
    <td align="right">2.61</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.96</td>
    <td align="right">2.50</td>
    <td align="right">2.51</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.63</td>
    <td align="right">4.04</td>
    <td align="right">4.10</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.24</td>
    <td align="right">5.02</td>
    <td align="right">4.89</td>
    <td align="right">4.86</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.58</td>
    <td align="right">3.46</td>
    <td align="right">3.47</td>
    <td align="right">3.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.73</td>
    <td align="right">9.23</td>
    <td align="right">9.24</td>
    <td align="right">9.23</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.83</td>
    <td align="right">9.30</td>
    <td align="right">9.30</td>
    <td align="right">9.32</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.20</td>
    <td align="right">7.94</td>
    <td align="right">7.96</td>
    <td align="right">7.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.97</td>
    <td align="right">12.38</td>
    <td align="right">12.47</td>
    <td align="right">12.48</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.61</td>
    <td align="right">12.86</td>
    <td align="right">12.93</td>
    <td align="right">12.93</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.38</td>
    <td align="right">10.83</td>
    <td align="right">11.05</td>
    <td align="right">11.05</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">1.98</td>
    <td align="right">2.51</td>
    <td align="right">2.52</td>
    <td align="right">2.51</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.26</td>
    <td align="right">3.50</td>
    <td align="right">10.16</td>
    <td align="right">8.36</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.33</td>
    <td align="right">3.59</td>
    <td align="right">9.73</td>
    <td align="right">8.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.72</td>
    <td align="right">3.46</td>
    <td align="right">3.46</td>
    <td align="right">3.45</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.64</td>
    <td align="right">6.83</td>
    <td align="right">13.03</td>
    <td align="right">12.01</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.24</td>
    <td align="right">6.92</td>
    <td align="right">11.93</td>
    <td align="right">11.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.27</td>
    <td align="right">8.02</td>
    <td align="right">5.20</td>
    <td align="right">14.14</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.72</td>
    <td align="right">12.75</td>
    <td align="right">15.03</td>
    <td align="right">15.83</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.84</td>
    <td align="right">12.94</td>
    <td align="right">14.27</td>
    <td align="right">15.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.62</td>
    <td align="right">10.91</td>
    <td align="right">6.37</td>
    <td align="right">15.90</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.92</td>
    <td align="right">16.94</td>
    <td align="right">15.19</td>
    <td align="right">19.40</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">18.54</td>
    <td align="right">15.80</td>
    <td align="right">20.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">1.98</td>
    <td align="right">2.50</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.26</td>
    <td align="right">2.52</td>
    <td align="right">2.55</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.34</td>
    <td align="right">2.58</td>
    <td align="right">2.61</td>
    <td align="right">2.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.73</td>
    <td align="right">3.48</td>
    <td align="right">3.44</td>
    <td align="right">3.46</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.66</td>
    <td align="right">4.07</td>
    <td align="right">4.05</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.24</td>
    <td align="right">4.99</td>
    <td align="right">4.90</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.28</td>
    <td align="right">8.00</td>
    <td align="right">8.13</td>
    <td align="right">8.01</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.73</td>
    <td align="right">9.24</td>
    <td align="right">9.24</td>
    <td align="right">9.24</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.83</td>
    <td align="right">9.35</td>
    <td align="right">9.29</td>
    <td align="right">9.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.61</td>
    <td align="right">11.03</td>
    <td align="right">11.18</td>
    <td align="right">11.19</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.94</td>
    <td align="right">12.35</td>
    <td align="right">12.47</td>
    <td align="right">12.50</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.58</td>
    <td align="right">12.89</td>
    <td align="right">12.93</td>
    <td align="right">12.92</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.54</td>
    <td align="right">4.41</td>
    <td align="right">11.09</td>
    <td align="right">9.67</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.49</td>
    <td align="right">4.73</td>
    <td align="right">13.30</td>
    <td align="right">10.37</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.77</td>
    <td align="right">6.51</td>
    <td align="right">14.59</td>
    <td align="right">10.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.44</td>
    <td align="right">7.52</td>
    <td align="right">11.88</td>
    <td align="right">12.86</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.42</td>
    <td align="right">8.07</td>
    <td align="right">12.06</td>
    <td align="right">13.53</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.90</td>
    <td align="right">11.59</td>
    <td align="right">16.61</td>
    <td align="right">15.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.52</td>
    <td align="right">12.41</td>
    <td align="right">13.38</td>
    <td align="right">16.57</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.04</td>
    <td align="right">14.53</td>
    <td align="right">15.48</td>
    <td align="right">18.80</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.95</td>
    <td align="right">19.42</td>
    <td align="right">15.46</td>
    <td align="right">19.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.64</td>
    <td align="right">16.32</td>
    <td align="right">15.08</td>
    <td align="right">20.26</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.91</td>
    <td align="right">19.55</td>
    <td align="right">16.40</td>
    <td align="right">23.31</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.34</td>
    <td align="right">35.71</td>
    <td align="right">17.51</td>
    <td align="right">31.10</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.54</td>
    <td align="right">4.27</td>
    <td align="right">4.35</td>
    <td align="right">4.36</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.48</td>
    <td align="right">5.00</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.77</td>
    <td align="right">6.31</td>
    <td align="right">6.31</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.43</td>
    <td align="right">7.80</td>
    <td align="right">7.84</td>
    <td align="right">7.85</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.12</td>
    <td align="right">8.31</td>
    <td align="right">8.25</td>
    <td align="right">8.22</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.89</td>
    <td align="right">12.18</td>
    <td align="right">12.09</td>
    <td align="right">12.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.57</td>
    <td align="right">13.13</td>
    <td align="right">13.19</td>
    <td align="right">13.24</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.01</td>
    <td align="right">15.46</td>
    <td align="right">15.52</td>
    <td align="right">15.46</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.95</td>
    <td align="right">20.72</td>
    <td align="right">20.72</td>
    <td align="right">20.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.76</td>
    <td align="right">17.82</td>
    <td align="right">18.16</td>
    <td align="right">18.15</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.89</td>
    <td align="right">21.31</td>
    <td align="right">21.65</td>
    <td align="right">21.64</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.40</td>
    <td align="right">36.95</td>
    <td align="right">36.96</td>
    <td align="right">36.99</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.19</td>
    <td align="right">4.97</td>
    <td align="right">3.42</td>
    <td align="right">10.69</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.16</td>
    <td align="right">11.86</td>
    <td align="right">15.65</td>
    <td align="right">14.84</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.86</td>
    <td align="right">3.78</td>
    <td align="right">3.92</td>
    <td align="right">8.54</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.42</td>
    <td align="right">4.11</td>
    <td align="right">4.27</td>
    <td align="right">8.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.07</td>
    <td align="right">16.95</td>
    <td align="right">16.01</td>
    <td align="right">17.44</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.52</td>
    <td align="right">4.17</td>
    <td align="right">4.07</td>
    <td align="right">8.89</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.05</td>
    <td align="right">4.52</td>
    <td align="right">4.43</td>
    <td align="right">9.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.69</td>
    <td align="right">21.15</td>
    <td align="right">15.85</td>
    <td align="right">20.10</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.21</td>
    <td align="right">4.53</td>
    <td align="right">4.39</td>
    <td align="right">9.34</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.79</td>
    <td align="right">4.86</td>
    <td align="right">4.70</td>
    <td align="right">9.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.63</td>
    <td align="right">26.38</td>
    <td align="right">15.98</td>
    <td align="right">23.03</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">7.83</td>
    <td align="right">4.91</td>
    <td align="right">4.73</td>
    <td align="right">9.77</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">8.97</td>
    <td align="right">5.20</td>
    <td align="right">5.11</td>
    <td align="right">10.19</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.20</td>
    <td align="right">13.10</td>
    <td align="right">13.14</td>
    <td align="right">18.57</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.89</td>
    <td align="right">3.77</td>
    <td align="right">3.92</td>
    <td align="right">8.58</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">4.11</td>
    <td align="right">4.27</td>
    <td align="right">8.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.94</td>
    <td align="right">19.15</td>
    <td align="right">18.89</td>
    <td align="right">24.50</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.51</td>
    <td align="right">4.15</td>
    <td align="right">4.04</td>
    <td align="right">8.78</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">4.49</td>
    <td align="right">4.34</td>
    <td align="right">9.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.19</td>
    <td align="right">23.40</td>
    <td align="right">23.19</td>
    <td align="right">28.67</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.34</td>
    <td align="right">4.53</td>
    <td align="right">4.40</td>
    <td align="right">9.43</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.64</td>
    <td align="right">4.92</td>
    <td align="right">4.70</td>
    <td align="right">9.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">34.81</td>
    <td align="right">58.69</td>
    <td align="right">75.75</td>
    <td align="right">70.29</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.99</td>
    <td align="right">4.87</td>
    <td align="right">4.70</td>
    <td align="right">9.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">8.50</td>
    <td align="right">5.24</td>
    <td align="right">5.12</td>
    <td align="right">10.31</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.38</td>
    <td align="right">7.03</td>
    <td align="right">11.33</td>
    <td align="right">10.91</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.54</td>
    <td align="right">7.58</td>
    <td align="right">12.35</td>
    <td align="right">11.68</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.84</td>
    <td align="right">2.47</td>
    <td align="right">2.79</td>
    <td align="right">8.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.16</td>
    <td align="right">9.88</td>
    <td align="right">11.92</td>
    <td align="right">12.43</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.57</td>
    <td align="right">10.90</td>
    <td align="right">13.11</td>
    <td align="right">14.07</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">3.33</td>
    <td align="right">2.53</td>
    <td align="right">9.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.49</td>
    <td align="right">13.12</td>
    <td align="right">14.43</td>
    <td align="right">15.62</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.22</td>
    <td align="right">14.01</td>
    <td align="right">15.32</td>
    <td align="right">16.57</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.30</td>
    <td align="right">4.76</td>
    <td align="right">3.29</td>
    <td align="right">11.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">15.03</td>
    <td align="right">14.82</td>
    <td align="right">14.05</td>
    <td align="right">17.62</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">17.38</td>
    <td align="right">29.69</td>
    <td align="right">21.03</td>
    <td align="right">29.43</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.75</td>
    <td align="right">4.80</td>
    <td align="right">3.27</td>
    <td align="right">11.35</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.45</td>
    <td align="right">4.96</td>
    <td align="right">5.05</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.52</td>
    <td align="right">5.37</td>
    <td align="right">5.49</td>
    <td align="right">11.05</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.83</td>
    <td align="right">2.63</td>
    <td align="right">2.82</td>
    <td align="right">8.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.13</td>
    <td align="right">7.26</td>
    <td align="right">6.69</td>
    <td align="right">11.67</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.65</td>
    <td align="right">7.67</td>
    <td align="right">7.57</td>
    <td align="right">13.20</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.57</td>
    <td align="right">2.41</td>
    <td align="right">8.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.50</td>
    <td align="right">9.25</td>
    <td align="right">8.94</td>
    <td align="right">14.13</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.26</td>
    <td align="right">10.80</td>
    <td align="right">10.46</td>
    <td align="right">15.91</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">3.81</td>
    <td align="right">3.61</td>
    <td align="right">10.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">13.92</td>
    <td align="right">13.61</td>
    <td align="right">15.12</td>
    <td align="right">21.41</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.20</td>
    <td align="right">18.21</td>
    <td align="right">17.89</td>
    <td align="right">22.74</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.37</td>
    <td align="right">3.89</td>
    <td align="right">3.67</td>
    <td align="right">10.46</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.71</td>
    <td align="right">2.34</td>
    <td align="right">2.61</td>
    <td align="right">8.97</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.65</td>
    <td align="right">3.43</td>
    <td align="right">3.74</td>
    <td align="right">10.38</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">3.31</td>
    <td align="right">3.61</td>
    <td align="right">10.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.20</td>
    <td align="right">3.76</td>
    <td align="right">2.92</td>
    <td align="right">9.58</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.21</td>
    <td align="right">4.18</td>
    <td align="right">3.42</td>
    <td align="right">10.50</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.76</td>
    <td align="right">5.19</td>
    <td align="right">4.18</td>
    <td align="right">11.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.34</td>
    <td align="right">4.61</td>
    <td align="right">3.11</td>
    <td align="right">10.92</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.14</td>
    <td align="right">6.50</td>
    <td align="right">4.97</td>
    <td align="right">13.42</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.63</td>
    <td align="right">6.45</td>
    <td align="right">5.04</td>
    <td align="right">12.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.38</td>
    <td align="right">4.65</td>
    <td align="right">3.14</td>
    <td align="right">11.22</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.45</td>
    <td align="right">7.25</td>
    <td align="right">4.97</td>
    <td align="right">13.78</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.01</td>
    <td align="right">7.20</td>
    <td align="right">5.04</td>
    <td align="right">13.46</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.71</td>
    <td align="right">2.49</td>
    <td align="right">2.64</td>
    <td align="right">8.72</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.64</td>
    <td align="right">3.48</td>
    <td align="right">3.73</td>
    <td align="right">10.51</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.75</td>
    <td align="right">3.37</td>
    <td align="right">3.57</td>
    <td align="right">10.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.19</td>
    <td align="right">2.57</td>
    <td align="right">2.38</td>
    <td align="right">8.55</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.21</td>
    <td align="right">4.75</td>
    <td align="right">4.55</td>
    <td align="right">10.96</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.72</td>
    <td align="right">5.36</td>
    <td align="right">5.21</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.33</td>
    <td align="right">3.60</td>
    <td align="right">3.39</td>
    <td align="right">10.01</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.41</td>
    <td align="right">7.07</td>
    <td align="right">6.89</td>
    <td align="right">13.91</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.61</td>
    <td align="right">6.71</td>
    <td align="right">6.56</td>
    <td align="right">13.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.38</td>
    <td align="right">3.62</td>
    <td align="right">3.43</td>
    <td align="right">10.57</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.61</td>
    <td align="right">8.07</td>
    <td align="right">7.76</td>
    <td align="right">14.87</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.97</td>
    <td align="right">7.55</td>
    <td align="right">7.35</td>
    <td align="right">14.57</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.32</td>
    <td align="right">7.10</td>
    <td align="right">11.69</td>
    <td align="right">11.33</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">9.99</td>
    <td align="right">9.61</td>
    <td align="right">13.92</td>
    <td align="right">12.99</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.16</td>
    <td align="right">12.56</td>
    <td align="right">16.59</td>
    <td align="right">15.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.68</td>
    <td align="right">10.07</td>
    <td align="right">12.32</td>
    <td align="right">13.55</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.80</td>
    <td align="right">11.37</td>
    <td align="right">13.46</td>
    <td align="right">14.76</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.90</td>
    <td align="right">16.47</td>
    <td align="right">16.35</td>
    <td align="right">18.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">12.12</td>
    <td align="right">14.43</td>
    <td align="right">15.13</td>
    <td align="right">18.73</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.30</td>
    <td align="right">13.18</td>
    <td align="right">12.75</td>
    <td align="right">15.28</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.28</td>
    <td align="right">18.22</td>
    <td align="right">14.83</td>
    <td align="right">19.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.78</td>
    <td align="right">22.11</td>
    <td align="right">16.72</td>
    <td align="right">24.71</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.88</td>
    <td align="right">26.75</td>
    <td align="right">17.34</td>
    <td align="right">27.72</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.91</td>
    <td align="right">49.16</td>
    <td align="right">18.92</td>
    <td align="right">40.00</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.37</td>
    <td align="right">6.59</td>
    <td align="right">6.29</td>
    <td align="right">11.25</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">9.82</td>
    <td align="right">7.83</td>
    <td align="right">7.94</td>
    <td align="right">12.88</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.14</td>
    <td align="right">9.42</td>
    <td align="right">9.53</td>
    <td align="right">14.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.69</td>
    <td align="right">8.62</td>
    <td align="right">8.33</td>
    <td align="right">13.45</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.85</td>
    <td align="right">9.78</td>
    <td align="right">8.92</td>
    <td align="right">14.58</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.80</td>
    <td align="right">13.55</td>
    <td align="right">13.49</td>
    <td align="right">18.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.90</td>
    <td align="right">15.36</td>
    <td align="right">15.22</td>
    <td align="right">19.82</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.21</td>
    <td align="right">13.24</td>
    <td align="right">13.16</td>
    <td align="right">17.25</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.49</td>
    <td align="right">26.93</td>
    <td align="right">24.82</td>
    <td align="right">28.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.31</td>
    <td align="right">19.56</td>
    <td align="right">19.53</td>
    <td align="right">24.07</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.97</td>
    <td align="right">15.04</td>
    <td align="right">15.03</td>
    <td align="right">18.52</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">25.64</td>
    <td align="right">22.84</td>
    <td align="right">22.37</td>
    <td align="right">27.06</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.55</td>
    <td align="right">23.45</td>
    <td align="right">14.36</td>
    <td align="right">28.38</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">28.14</td>
    <td align="right">12.37</td>
    <td align="right">17.47</td>
    <td align="right">15.73</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.24</td>
    <td align="right">4.04</td>
    <td align="right">4.23</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.76</td>
    <td align="right">12.64</td>
    <td align="right">12.75</td>
    <td align="right">16.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">43.28</td>
    <td align="right">85.33</td>
    <td align="right">38.96</td>
    <td align="right">63.48</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.91</td>
    <td align="right">6.70</td>
    <td align="right">6.56</td>
    <td align="right">11.58</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.96</td>
    <td align="right">6.29</td>
    <td align="right">6.15</td>
    <td align="right">10.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">73.18</td>
    <td align="right">92.09</td>
    <td align="right">31.96</td>
    <td align="right">63.54</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.43</td>
    <td align="right">15.82</td>
    <td align="right">15.68</td>
    <td align="right">19.88</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.90</td>
    <td align="right">16.19</td>
    <td align="right">15.93</td>
    <td align="right">19.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.54</td>
    <td align="right">130.67</td>
    <td align="right">37.21</td>
    <td align="right">85.72</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.99</td>
    <td align="right">19.16</td>
    <td align="right">18.87</td>
    <td align="right">22.88</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.83</td>
    <td align="right">22.73</td>
    <td align="right">22.47</td>
    <td align="right">26.43</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">19.70</td>
    <td align="right">13.71</td>
    <td align="right">13.72</td>
    <td align="right">19.29</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.22</td>
    <td align="right">4.05</td>
    <td align="right">4.24</td>
    <td align="right">9.48</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.79</td>
    <td align="right">13.48</td>
    <td align="right">13.49</td>
    <td align="right">17.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">34.60</td>
    <td align="right">23.18</td>
    <td align="right">23.05</td>
    <td align="right">28.22</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.36</td>
    <td align="right">6.33</td>
    <td align="right">6.25</td>
    <td align="right">11.34</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.98</td>
    <td align="right">17.12</td>
    <td align="right">17.13</td>
    <td align="right">20.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">73.34</td>
    <td align="right">99.50</td>
    <td align="right">99.56</td>
    <td align="right">104.19</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.57</td>
    <td align="right">15.67</td>
    <td align="right">15.57</td>
    <td align="right">19.76</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.33</td>
    <td align="right">15.52</td>
    <td align="right">15.39</td>
    <td align="right">19.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.12</td>
    <td align="right">143.19</td>
    <td align="right">142.91</td>
    <td align="right">146.95</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.56</td>
    <td align="right">18.62</td>
    <td align="right">18.33</td>
    <td align="right">22.68</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.80</td>
    <td align="right">22.67</td>
    <td align="right">22.55</td>
    <td align="right">26.61</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.14</td>
    <td align="right">7.71</td>
    <td align="right">12.03</td>
    <td align="right">11.85</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.64</td>
    <td align="right">8.29</td>
    <td align="right">13.07</td>
    <td align="right">12.46</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.10</td>
    <td align="right">2.66</td>
    <td align="right">3.15</td>
    <td align="right">9.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">11.99</td>
    <td align="right">13.96</td>
    <td align="right">14.81</td>
    <td align="right">16.57</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.25</td>
    <td align="right">34.00</td>
    <td align="right">23.35</td>
    <td align="right">34.23</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.10</td>
    <td align="right">6.33</td>
    <td align="right">5.37</td>
    <td align="right">11.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.24</td>
    <td align="right">29.90</td>
    <td align="right">23.38</td>
    <td align="right">30.46</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.95</td>
    <td align="right">32.31</td>
    <td align="right">26.72</td>
    <td align="right">34.05</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.47</td>
    <td align="right">16.05</td>
    <td align="right">12.15</td>
    <td align="right">18.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.62</td>
    <td align="right">46.38</td>
    <td align="right">26.19</td>
    <td align="right">46.37</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.54</td>
    <td align="right">55.26</td>
    <td align="right">30.27</td>
    <td align="right">53.40</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.91</td>
    <td align="right">18.12</td>
    <td align="right">13.57</td>
    <td align="right">21.07</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.03</td>
    <td align="right">15.74</td>
    <td align="right">15.64</td>
    <td align="right">19.39</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.70</td>
    <td align="right">5.75</td>
    <td align="right">5.89</td>
    <td align="right">11.83</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">7.84</td>
    <td align="right">6.90</td>
    <td align="right">6.70</td>
    <td align="right">11.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.26</td>
    <td align="right">9.52</td>
    <td align="right">8.79</td>
    <td align="right">13.88</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.75</td>
    <td align="right">25.37</td>
    <td align="right">25.20</td>
    <td align="right">30.10</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">5.32</td>
    <td align="right">4.80</td>
    <td align="right">4.62</td>
    <td align="right">10.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">28.01</td>
    <td align="right">29.53</td>
    <td align="right">29.33</td>
    <td align="right">33.75</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.74</td>
    <td align="right">28.27</td>
    <td align="right">28.09</td>
    <td align="right">32.86</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.13</td>
    <td align="right">13.48</td>
    <td align="right">13.29</td>
    <td align="right">17.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.49</td>
    <td align="right">34.71</td>
    <td align="right">34.65</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.45</td>
    <td align="right">37.83</td>
    <td align="right">37.43</td>
    <td align="right">41.92</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.74</td>
    <td align="right">15.35</td>
    <td align="right">15.15</td>
    <td align="right">19.94</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.05</td>
    <td align="right">2.51</td>
    <td align="right">2.94</td>
    <td align="right">9.63</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.09</td>
    <td align="right">3.73</td>
    <td align="right">4.04</td>
    <td align="right">11.13</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.12</td>
    <td align="right">3.54</td>
    <td align="right">3.93</td>
    <td align="right">10.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.73</td>
    <td align="right">6.30</td>
    <td align="right">5.25</td>
    <td align="right">11.35</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.04</td>
    <td align="right">6.00</td>
    <td align="right">5.35</td>
    <td align="right">12.28</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">20.71</td>
    <td align="right">18.96</td>
    <td align="right">16.17</td>
    <td align="right">21.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.42</td>
    <td align="right">16.03</td>
    <td align="right">12.04</td>
    <td align="right">18.52</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.07</td>
    <td align="right">19.31</td>
    <td align="right">16.14</td>
    <td align="right">22.60</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.30</td>
    <td align="right">18.78</td>
    <td align="right">15.88</td>
    <td align="right">22.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.80</td>
    <td align="right">18.03</td>
    <td align="right">13.39</td>
    <td align="right">20.34</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.74</td>
    <td align="right">26.82</td>
    <td align="right">18.70</td>
    <td align="right">26.94</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.75</td>
    <td align="right">27.32</td>
    <td align="right">19.10</td>
    <td align="right">26.95</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.08</td>
    <td align="right">2.74</td>
    <td align="right">2.95</td>
    <td align="right">9.35</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">10.50</td>
    <td align="right">11.87</td>
    <td align="right">11.93</td>
    <td align="right">16.59</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.11</td>
    <td align="right">3.57</td>
    <td align="right">3.91</td>
    <td align="right">10.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">6.02</td>
    <td align="right">4.69</td>
    <td align="right">4.31</td>
    <td align="right">9.82</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">7.44</td>
    <td align="right">7.82</td>
    <td align="right">7.45</td>
    <td align="right">13.89</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.53</td>
    <td align="right">8.54</td>
    <td align="right">8.26</td>
    <td align="right">14.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.96</td>
    <td align="right">13.16</td>
    <td align="right">13.02</td>
    <td align="right">17.17</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.94</td>
    <td align="right">22.01</td>
    <td align="right">21.73</td>
    <td align="right">26.50</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.17</td>
    <td align="right">21.73</td>
    <td align="right">19.70</td>
    <td align="right">25.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.90</td>
    <td align="right">15.33</td>
    <td align="right">15.20</td>
    <td align="right">19.71</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.68</td>
    <td align="right">27.38</td>
    <td align="right">27.28</td>
    <td align="right">32.21</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.80</td>
    <td align="right">27.92</td>
    <td align="right">27.69</td>
    <td align="right">32.40</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.93</td>
    <td align="right">19.62</td>
    <td align="right">19.22</td>
    <td align="right">22.70</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.51</td>
    <td align="right">10.69</td>
    <td align="right">14.74</td>
    <td align="right">14.17</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.74</td>
    <td align="right">13.98</td>
    <td align="right">17.65</td>
    <td align="right">16.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">13.80</td>
    <td align="right">13.50</td>
    <td align="right">14.52</td>
    <td align="right">16.65</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">16.61</td>
    <td align="right">16.43</td>
    <td align="right">15.95</td>
    <td align="right">18.91</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.58</td>
    <td align="right">18.37</td>
    <td align="right">17.46</td>
    <td align="right">20.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.59</td>
    <td align="right">27.76</td>
    <td align="right">21.10</td>
    <td align="right">29.84</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.29</td>
    <td align="right">31.75</td>
    <td align="right">20.18</td>
    <td align="right">32.29</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">39.70</td>
    <td align="right">44.65</td>
    <td align="right">23.19</td>
    <td align="right">40.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.11</td>
    <td align="right">53.53</td>
    <td align="right">25.65</td>
    <td align="right">55.07</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">41.93</td>
    <td align="right">40.84</td>
    <td align="right">22.44</td>
    <td align="right">41.43</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.90</td>
    <td align="right">65.99</td>
    <td align="right">27.47</td>
    <td align="right">56.61</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.15</td>
    <td align="right">7.16</td>
    <td align="right">6.78</td>
    <td align="right">12.03</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">14.34</td>
    <td align="right">8.40</td>
    <td align="right">8.52</td>
    <td align="right">13.75</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.30</td>
    <td align="right">10.49</td>
    <td align="right">10.59</td>
    <td align="right">16.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.57</td>
    <td align="right">16.25</td>
    <td align="right">16.13</td>
    <td align="right">21.21</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.71</td>
    <td align="right">12.68</td>
    <td align="right">11.72</td>
    <td align="right">17.77</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">22.96</td>
    <td align="right">15.48</td>
    <td align="right">15.48</td>
    <td align="right">20.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.09</td>
    <td align="right">26.16</td>
    <td align="right">26.10</td>
    <td align="right">30.61</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.68</td>
    <td align="right">32.65</td>
    <td align="right">33.39</td>
    <td align="right">36.33</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">39.93</td>
    <td align="right">39.26</td>
    <td align="right">38.88</td>
    <td align="right">42.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.54</td>
    <td align="right">34.73</td>
    <td align="right">34.65</td>
    <td align="right">39.16</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">41.93</td>
    <td align="right">40.18</td>
    <td align="right">40.11</td>
    <td align="right">43.28</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.02</td>
    <td align="right">63.93</td>
    <td align="right">63.51</td>
    <td align="right">67.00</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.68</td>
    <td align="right">13.55</td>
    <td align="right">7.75</td>
    <td align="right">16.70</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.87</td>
    <td align="right">44.30</td>
    <td align="right">38.33</td>
    <td align="right">42.11</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.35</td>
    <td align="right">18.88</td>
    <td align="right">19.02</td>
    <td align="right">27.01</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.55</td>
    <td align="right">21.98</td>
    <td align="right">22.64</td>
    <td align="right">30.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">45.75</td>
    <td align="right">66.40</td>
    <td align="right">41.83</td>
    <td align="right">53.94</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.46</td>
    <td align="right">22.87</td>
    <td align="right">23.16</td>
    <td align="right">32.00</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.08</td>
    <td align="right">20.78</td>
    <td align="right">20.72</td>
    <td align="right">29.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.29</td>
    <td align="right">83.34</td>
    <td align="right">40.07</td>
    <td align="right">62.51</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.52</td>
    <td align="right">21.11</td>
    <td align="right">20.86</td>
    <td align="right">30.48</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.06</td>
    <td align="right">23.50</td>
    <td align="right">23.56</td>
    <td align="right">32.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">71.81</td>
    <td align="right">104.15</td>
    <td align="right">41.35</td>
    <td align="right">72.54</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.79</td>
    <td align="right">23.84</td>
    <td align="right">23.88</td>
    <td align="right">33.27</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.06</td>
    <td align="right">25.01</td>
    <td align="right">24.74</td>
    <td align="right">34.05</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">31.00</td>
    <td align="right">46.43</td>
    <td align="right">45.75</td>
    <td align="right">55.02</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.37</td>
    <td align="right">19.16</td>
    <td align="right">19.12</td>
    <td align="right">27.12</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.58</td>
    <td align="right">22.11</td>
    <td align="right">22.59</td>
    <td align="right">30.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.37</td>
    <td align="right">69.20</td>
    <td align="right">65.95</td>
    <td align="right">76.22</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.48</td>
    <td align="right">23.01</td>
    <td align="right">23.23</td>
    <td align="right">31.94</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">20.79</td>
    <td align="right">20.61</td>
    <td align="right">30.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.36</td>
    <td align="right">86.84</td>
    <td align="right">84.16</td>
    <td align="right">94.51</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.53</td>
    <td align="right">21.12</td>
    <td align="right">20.88</td>
    <td align="right">30.66</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.19</td>
    <td align="right">23.51</td>
    <td align="right">23.61</td>
    <td align="right">32.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">71.51</td>
    <td align="right">110.90</td>
    <td align="right">117.02</td>
    <td align="right">118.32</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.77</td>
    <td align="right">23.83</td>
    <td align="right">23.84</td>
    <td align="right">33.25</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.48</td>
    <td align="right">25.02</td>
    <td align="right">24.72</td>
    <td align="right">34.04</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.93</td>
    <td align="right">23.76</td>
    <td align="right">27.30</td>
    <td align="right">28.50</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.19</td>
    <td align="right">27.27</td>
    <td align="right">29.28</td>
    <td align="right">30.56</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.85</td>
    <td align="right">15.15</td>
    <td align="right">24.35</td>
    <td align="right">22.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.77</td>
    <td align="right">30.58</td>
    <td align="right">28.51</td>
    <td align="right">31.66</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.00</td>
    <td align="right">34.42</td>
    <td align="right">33.94</td>
    <td align="right">35.80</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.18</td>
    <td align="right">19.20</td>
    <td align="right">26.46</td>
    <td align="right">25.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.79</td>
    <td align="right">44.73</td>
    <td align="right">30.64</td>
    <td align="right">39.78</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.86</td>
    <td align="right">49.81</td>
    <td align="right">39.66</td>
    <td align="right">44.91</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.49</td>
    <td align="right">21.58</td>
    <td align="right">27.13</td>
    <td align="right">27.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.66</td>
    <td align="right">49.17</td>
    <td align="right">29.64</td>
    <td align="right">44.36</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.52</td>
    <td align="right">57.95</td>
    <td align="right">41.91</td>
    <td align="right">49.85</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.27</td>
    <td align="right">29.19</td>
    <td align="right">26.71</td>
    <td align="right">30.65</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.80</td>
    <td align="right">23.65</td>
    <td align="right">23.72</td>
    <td align="right">30.24</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">26.81</td>
    <td align="right">26.78</td>
    <td align="right">33.04</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.90</td>
    <td align="right">16.43</td>
    <td align="right">16.47</td>
    <td align="right">23.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.62</td>
    <td align="right">32.31</td>
    <td align="right">31.92</td>
    <td align="right">36.33</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.97</td>
    <td align="right">35.13</td>
    <td align="right">34.82</td>
    <td align="right">39.66</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.13</td>
    <td align="right">19.18</td>
    <td align="right">18.61</td>
    <td align="right">25.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.62</td>
    <td align="right">38.53</td>
    <td align="right">38.26</td>
    <td align="right">42.17</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.53</td>
    <td align="right">49.57</td>
    <td align="right">49.21</td>
    <td align="right">54.16</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.34</td>
    <td align="right">21.94</td>
    <td align="right">21.10</td>
    <td align="right">28.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.27</td>
    <td align="right">44.04</td>
    <td align="right">43.55</td>
    <td align="right">47.64</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.34</td>
    <td align="right">58.58</td>
    <td align="right">58.28</td>
    <td align="right">63.05</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.88</td>
    <td align="right">26.48</td>
    <td align="right">26.19</td>
    <td align="right">33.37</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.54</td>
    <td align="right">16.67</td>
    <td align="right">25.01</td>
    <td align="right">23.13</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.78</td>
    <td align="right">23.69</td>
    <td align="right">27.29</td>
    <td align="right">28.27</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">28.18</td>
    <td align="right">29.28</td>
    <td align="right">30.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.04</td>
    <td align="right">19.98</td>
    <td align="right">27.78</td>
    <td align="right">25.73</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.79</td>
    <td align="right">30.63</td>
    <td align="right">28.69</td>
    <td align="right">31.77</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.94</td>
    <td align="right">34.37</td>
    <td align="right">33.90</td>
    <td align="right">35.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.44</td>
    <td align="right">22.91</td>
    <td align="right">28.15</td>
    <td align="right">28.05</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.23</td>
    <td align="right">44.83</td>
    <td align="right">30.63</td>
    <td align="right">39.97</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.85</td>
    <td align="right">49.79</td>
    <td align="right">39.67</td>
    <td align="right">44.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.71</td>
    <td align="right">30.80</td>
    <td align="right">28.83</td>
    <td align="right">32.73</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.61</td>
    <td align="right">48.03</td>
    <td align="right">30.21</td>
    <td align="right">42.48</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.54</td>
    <td align="right">57.93</td>
    <td align="right">41.89</td>
    <td align="right">49.85</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.50</td>
    <td align="right">17.42</td>
    <td align="right">17.22</td>
    <td align="right">24.16</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.86</td>
    <td align="right">23.64</td>
    <td align="right">23.72</td>
    <td align="right">30.23</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.19</td>
    <td align="right">26.82</td>
    <td align="right">26.85</td>
    <td align="right">33.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.06</td>
    <td align="right">21.58</td>
    <td align="right">21.22</td>
    <td align="right">27.54</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.70</td>
    <td align="right">32.26</td>
    <td align="right">31.87</td>
    <td align="right">36.27</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.99</td>
    <td align="right">35.14</td>
    <td align="right">34.77</td>
    <td align="right">39.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.57</td>
    <td align="right">24.45</td>
    <td align="right">24.12</td>
    <td align="right">31.08</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.79</td>
    <td align="right">38.59</td>
    <td align="right">38.17</td>
    <td align="right">42.37</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.49</td>
    <td align="right">49.50</td>
    <td align="right">49.23</td>
    <td align="right">54.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.83</td>
    <td align="right">34.29</td>
    <td align="right">33.93</td>
    <td align="right">39.18</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.49</td>
    <td align="right">44.04</td>
    <td align="right">43.51</td>
    <td align="right">47.56</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.41</td>
    <td align="right">58.64</td>
    <td align="right">58.33</td>
    <td align="right">62.80</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.39</td>
    <td align="right">24.43</td>
    <td align="right">27.97</td>
    <td align="right">28.28</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.14</td>
    <td align="right">31.77</td>
    <td align="right">36.33</td>
    <td align="right">33.83</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.43</td>
    <td align="right">37.69</td>
    <td align="right">36.71</td>
    <td align="right">36.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.39</td>
    <td align="right">37.54</td>
    <td align="right">28.53</td>
    <td align="right">36.41</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.27</td>
    <td align="right">41.22</td>
    <td align="right">34.63</td>
    <td align="right">39.75</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">41.38</td>
    <td align="right">47.67</td>
    <td align="right">35.20</td>
    <td align="right">43.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.14</td>
    <td align="right">44.14</td>
    <td align="right">28.19</td>
    <td align="right">40.49</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.48</td>
    <td align="right">50.18</td>
    <td align="right">35.63</td>
    <td align="right">44.67</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.95</td>
    <td align="right">51.90</td>
    <td align="right">33.15</td>
    <td align="right">45.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.27</td>
    <td align="right">49.74</td>
    <td align="right">29.50</td>
    <td align="right">42.53</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.34</td>
    <td align="right">52.92</td>
    <td align="right">35.90</td>
    <td align="right">46.16</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.95</td>
    <td align="right">65.51</td>
    <td align="right">33.31</td>
    <td align="right">52.65</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.45</td>
    <td align="right">24.69</td>
    <td align="right">24.57</td>
    <td align="right">30.46</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.10</td>
    <td align="right">32.69</td>
    <td align="right">32.68</td>
    <td align="right">37.34</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.20</td>
    <td align="right">35.53</td>
    <td align="right">35.18</td>
    <td align="right">41.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.28</td>
    <td align="right">33.61</td>
    <td align="right">33.25</td>
    <td align="right">38.28</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.34</td>
    <td align="right">39.96</td>
    <td align="right">39.67</td>
    <td align="right">45.18</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.51</td>
    <td align="right">45.23</td>
    <td align="right">44.57</td>
    <td align="right">52.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.11</td>
    <td align="right">41.55</td>
    <td align="right">41.11</td>
    <td align="right">46.28</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.47</td>
    <td align="right">49.61</td>
    <td align="right">49.16</td>
    <td align="right">54.07</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.34</td>
    <td align="right">49.92</td>
    <td align="right">48.51</td>
    <td align="right">54.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.25</td>
    <td align="right">47.10</td>
    <td align="right">46.50</td>
    <td align="right">51.27</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.34</td>
    <td align="right">52.91</td>
    <td align="right">52.67</td>
    <td align="right">57.50</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.60</td>
    <td align="right">68.54</td>
    <td align="right">66.42</td>
    <td align="right">74.42</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.11</td>
    <td align="right">69.38</td>
    <td align="right">22.40</td>
    <td align="right">55.65</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">38.92</td>
    <td align="right">54.49</td>
    <td align="right">45.63</td>
    <td align="right">50.05</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.39</td>
    <td align="right">22.04</td>
    <td align="right">21.65</td>
    <td align="right">30.28</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.14</td>
    <td align="right">27.67</td>
    <td align="right">28.52</td>
    <td align="right">37.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">92.62</td>
    <td align="right">121.23</td>
    <td align="right">58.25</td>
    <td align="right">90.20</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.56</td>
    <td align="right">35.65</td>
    <td align="right">36.09</td>
    <td align="right">45.52</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.57</td>
    <td align="right">35.59</td>
    <td align="right">35.44</td>
    <td align="right">45.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">188.83</td>
    <td align="right">251.99</td>
    <td align="right">79.70</td>
    <td align="right">166.28</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.10</td>
    <td align="right">49.39</td>
    <td align="right">49.13</td>
    <td align="right">59.93</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.02</td>
    <td align="right">51.39</td>
    <td align="right">51.40</td>
    <td align="right">61.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.08</td>
    <td align="right">402.48</td>
    <td align="right">99.29</td>
    <td align="right">250.70</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.20</td>
    <td align="right">66.04</td>
    <td align="right">66.08</td>
    <td align="right">75.88</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.81</td>
    <td align="right">68.71</td>
    <td align="right">68.57</td>
    <td align="right">78.03</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">43.74</td>
    <td align="right">59.07</td>
    <td align="right">57.30</td>
    <td align="right">68.19</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.66</td>
    <td align="right">23.01</td>
    <td align="right">23.29</td>
    <td align="right">31.01</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">16.97</td>
    <td align="right">26.56</td>
    <td align="right">27.45</td>
    <td align="right">36.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">108.94</td>
    <td align="right">124.36</td>
    <td align="right">115.87</td>
    <td align="right">131.31</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.17</td>
    <td align="right">35.45</td>
    <td align="right">35.44</td>
    <td align="right">45.01</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.99</td>
    <td align="right">31.83</td>
    <td align="right">31.73</td>
    <td align="right">42.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">182.85</td>
    <td align="right">204.11</td>
    <td align="right">191.04</td>
    <td align="right">209.02</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.12</td>
    <td align="right">47.89</td>
    <td align="right">47.69</td>
    <td align="right">58.82</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.17</td>
    <td align="right">51.99</td>
    <td align="right">52.16</td>
    <td align="right">61.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">296.23</td>
    <td align="right">411.41</td>
    <td align="right">414.08</td>
    <td align="right">415.44</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.66</td>
    <td align="right">65.98</td>
    <td align="right">65.81</td>
    <td align="right">75.68</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.02</td>
    <td align="right">66.90</td>
    <td align="right">66.81</td>
    <td align="right">76.41</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.49</td>
    <td align="right">28.68</td>
    <td align="right">31.07</td>
    <td align="right">33.90</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.42</td>
    <td align="right">33.79</td>
    <td align="right">32.62</td>
    <td align="right">37.27</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">16.19</td>
    <td align="right">19.07</td>
    <td align="right">27.22</td>
    <td align="right">25.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.18</td>
    <td align="right">45.90</td>
    <td align="right">38.51</td>
    <td align="right">46.84</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.77</td>
    <td align="right">50.40</td>
    <td align="right">47.03</td>
    <td align="right">51.17</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.65</td>
    <td align="right">29.70</td>
    <td align="right">35.51</td>
    <td align="right">35.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.53</td>
    <td align="right">78.71</td>
    <td align="right">49.36</td>
    <td align="right">70.30</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.30</td>
    <td align="right">83.52</td>
    <td align="right">66.57</td>
    <td align="right">77.52</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.47</td>
    <td align="right">45.15</td>
    <td align="right">45.52</td>
    <td align="right">47.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.28</td>
    <td align="right">99.80</td>
    <td align="right">56.87</td>
    <td align="right">89.76</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.12</td>
    <td align="right">110.19</td>
    <td align="right">88.32</td>
    <td align="right">99.93</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.58</td>
    <td align="right">73.34</td>
    <td align="right">52.04</td>
    <td align="right">70.29</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.51</td>
    <td align="right">27.71</td>
    <td align="right">27.60</td>
    <td align="right">35.11</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.00</td>
    <td align="right">31.72</td>
    <td align="right">31.78</td>
    <td align="right">38.36</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.40</td>
    <td align="right">20.06</td>
    <td align="right">19.50</td>
    <td align="right">27.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">38.95</td>
    <td align="right">40.65</td>
    <td align="right">40.09</td>
    <td align="right">44.56</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.34</td>
    <td align="right">52.10</td>
    <td align="right">51.52</td>
    <td align="right">58.32</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.56</td>
    <td align="right">28.68</td>
    <td align="right">28.08</td>
    <td align="right">35.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.04</td>
    <td align="right">74.44</td>
    <td align="right">74.37</td>
    <td align="right">78.36</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.99</td>
    <td align="right">83.32</td>
    <td align="right">82.91</td>
    <td align="right">87.78</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.71</td>
    <td align="right">45.60</td>
    <td align="right">44.75</td>
    <td align="right">51.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.79</td>
    <td align="right">97.42</td>
    <td align="right">96.68</td>
    <td align="right">99.89</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">132.87</td>
    <td align="right">109.47</td>
    <td align="right">109.28</td>
    <td align="right">114.02</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.80</td>
    <td align="right">74.28</td>
    <td align="right">74.13</td>
    <td align="right">81.85</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.08</td>
    <td align="right">19.58</td>
    <td align="right">29.31</td>
    <td align="right">27.39</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.95</td>
    <td align="right">27.84</td>
    <td align="right">30.63</td>
    <td align="right">33.11</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.11</td>
    <td align="right">32.20</td>
    <td align="right">32.12</td>
    <td align="right">35.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.98</td>
    <td align="right">32.87</td>
    <td align="right">38.86</td>
    <td align="right">37.35</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.43</td>
    <td align="right">44.36</td>
    <td align="right">38.07</td>
    <td align="right">45.47</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.50</td>
    <td align="right">49.17</td>
    <td align="right">46.12</td>
    <td align="right">50.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.61</td>
    <td align="right">48.18</td>
    <td align="right">50.79</td>
    <td align="right">51.30</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.75</td>
    <td align="right">77.41</td>
    <td align="right">49.43</td>
    <td align="right">69.43</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.23</td>
    <td align="right">84.76</td>
    <td align="right">67.56</td>
    <td align="right">78.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.48</td>
    <td align="right">80.68</td>
    <td align="right">60.48</td>
    <td align="right">78.27</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.99</td>
    <td align="right">97.50</td>
    <td align="right">55.64</td>
    <td align="right">86.35</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.57</td>
    <td align="right">110.02</td>
    <td align="right">88.18</td>
    <td align="right">99.75</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.48</td>
    <td align="right">18.87</td>
    <td align="right">18.72</td>
    <td align="right">29.44</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.54</td>
    <td align="right">27.75</td>
    <td align="right">27.78</td>
    <td align="right">35.28</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.90</td>
    <td align="right">31.55</td>
    <td align="right">31.60</td>
    <td align="right">38.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.00</td>
    <td align="right">31.77</td>
    <td align="right">31.54</td>
    <td align="right">38.59</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.90</td>
    <td align="right">41.46</td>
    <td align="right">40.81</td>
    <td align="right">46.02</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.64</td>
    <td align="right">48.89</td>
    <td align="right">48.21</td>
    <td align="right">55.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">49.04</td>
    <td align="right">55.55</td>
    <td align="right">54.48</td>
    <td align="right">61.86</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.50</td>
    <td align="right">73.90</td>
    <td align="right">73.39</td>
    <td align="right">77.55</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">104.57</td>
    <td align="right">84.03</td>
    <td align="right">83.64</td>
    <td align="right">88.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.96</td>
    <td align="right">85.58</td>
    <td align="right">85.27</td>
    <td align="right">90.78</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.48</td>
    <td align="right">98.92</td>
    <td align="right">98.25</td>
    <td align="right">101.36</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.70</td>
    <td align="right">110.16</td>
    <td align="right">110.09</td>
    <td align="right">114.74</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.20</td>
    <td align="right">27.25</td>
    <td align="right">30.70</td>
    <td align="right">31.50</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.11</td>
    <td align="right">39.47</td>
    <td align="right">40.29</td>
    <td align="right">40.23</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.00</td>
    <td align="right">45.17</td>
    <td align="right">41.07</td>
    <td align="right">45.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.54</td>
    <td align="right">52.32</td>
    <td align="right">39.46</td>
    <td align="right">50.97</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.80</td>
    <td align="right">57.11</td>
    <td align="right">46.05</td>
    <td align="right">55.08</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">62.49</td>
    <td align="right">67.24</td>
    <td align="right">43.97</td>
    <td align="right">58.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.36</td>
    <td align="right">72.58</td>
    <td align="right">48.34</td>
    <td align="right">68.39</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.52</td>
    <td align="right">87.91</td>
    <td align="right">59.70</td>
    <td align="right">79.92</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.99</td>
    <td align="right">94.31</td>
    <td align="right">45.03</td>
    <td align="right">77.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.88</td>
    <td align="right">90.88</td>
    <td align="right">56.93</td>
    <td align="right">84.52</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.63</td>
    <td align="right">106.51</td>
    <td align="right">68.22</td>
    <td align="right">95.48</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.43</td>
    <td align="right">138.14</td>
    <td align="right">50.59</td>
    <td align="right">108.27</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.06</td>
    <td align="right">27.38</td>
    <td align="right">27.33</td>
    <td align="right">34.31</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">39.66</td>
    <td align="right">41.27</td>
    <td align="right">42.41</td>
    <td align="right">47.20</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.42</td>
    <td align="right">40.66</td>
    <td align="right">39.07</td>
    <td align="right">45.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">43.64</td>
    <td align="right">48.77</td>
    <td align="right">48.19</td>
    <td align="right">53.13</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.90</td>
    <td align="right">55.64</td>
    <td align="right">55.30</td>
    <td align="right">63.88</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.59</td>
    <td align="right">64.60</td>
    <td align="right">64.27</td>
    <td align="right">70.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.11</td>
    <td align="right">69.24</td>
    <td align="right">68.75</td>
    <td align="right">74.09</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.71</td>
    <td align="right">87.66</td>
    <td align="right">87.22</td>
    <td align="right">92.30</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">93.59</td>
    <td align="right">100.99</td>
    <td align="right">100.30</td>
    <td align="right">105.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.17</td>
    <td align="right">89.20</td>
    <td align="right">88.71</td>
    <td align="right">93.06</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.99</td>
    <td align="right">106.32</td>
    <td align="right">106.07</td>
    <td align="right">112.94</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">141.68</td>
    <td align="right">157.93</td>
    <td align="right">158.68</td>
    <td align="right">168.00</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.68</td>
    <td align="right">14.74</td>
    <td align="right">8.41</td>
    <td align="right">19.43</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.55</td>
    <td align="right">31.78</td>
    <td align="right">28.40</td>
    <td align="right">30.43</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.54</td>
    <td align="right">14.55</td>
    <td align="right">14.65</td>
    <td align="right">14.68</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">17.79</td>
    <td align="right">17.79</td>
    <td align="right">17.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.59</td>
    <td align="right">48.85</td>
    <td align="right">30.87</td>
    <td align="right">40.38</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.06</td>
    <td align="right">18.25</td>
    <td align="right">18.25</td>
    <td align="right">18.25</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.22</td>
    <td align="right">21.72</td>
    <td align="right">21.73</td>
    <td align="right">21.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.33</td>
    <td align="right">65.62</td>
    <td align="right">34.39</td>
    <td align="right">50.88</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.60</td>
    <td align="right">21.42</td>
    <td align="right">21.44</td>
    <td align="right">21.34</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.05</td>
    <td align="right">23.02</td>
    <td align="right">23.03</td>
    <td align="right">23.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">66.28</td>
    <td align="right">82.87</td>
    <td align="right">35.26</td>
    <td align="right">59.82</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.25</td>
    <td align="right">23.42</td>
    <td align="right">23.51</td>
    <td align="right">23.40</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">25.73</td>
    <td align="right">25.79</td>
    <td align="right">25.75</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.57</td>
    <td align="right">30.56</td>
    <td align="right">30.57</td>
    <td align="right">30.45</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.48</td>
    <td align="right">14.50</td>
    <td align="right">14.50</td>
    <td align="right">14.54</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.87</td>
    <td align="right">17.80</td>
    <td align="right">17.79</td>
    <td align="right">17.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.55</td>
    <td align="right">47.72</td>
    <td align="right">47.71</td>
    <td align="right">48.16</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.04</td>
    <td align="right">18.29</td>
    <td align="right">18.26</td>
    <td align="right">18.23</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.24</td>
    <td align="right">21.75</td>
    <td align="right">21.68</td>
    <td align="right">21.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.54</td>
    <td align="right">58.40</td>
    <td align="right">58.09</td>
    <td align="right">57.82</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.58</td>
    <td align="right">21.41</td>
    <td align="right">21.46</td>
    <td align="right">21.43</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.08</td>
    <td align="right">23.01</td>
    <td align="right">23.27</td>
    <td align="right">23.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">66.88</td>
    <td align="right">70.21</td>
    <td align="right">69.80</td>
    <td align="right">68.82</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.25</td>
    <td align="right">23.45</td>
    <td align="right">23.41</td>
    <td align="right">23.49</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.07</td>
    <td align="right">25.76</td>
    <td align="right">25.74</td>
    <td align="right">25.74</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.06</td>
    <td align="right">20.52</td>
    <td align="right">23.51</td>
    <td align="right">24.22</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.15</td>
    <td align="right">20.10</td>
    <td align="right">23.06</td>
    <td align="right">24.04</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.57</td>
    <td align="right">9.22</td>
    <td align="right">18.24</td>
    <td align="right">16.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.06</td>
    <td align="right">24.55</td>
    <td align="right">27.93</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.17</td>
    <td align="right">25.93</td>
    <td align="right">24.42</td>
    <td align="right">27.41</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">14.33</td>
    <td align="right">21.10</td>
    <td align="right">20.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.94</td>
    <td align="right">38.79</td>
    <td align="right">26.63</td>
    <td align="right">35.13</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">37.32</td>
    <td align="right">26.27</td>
    <td align="right">34.15</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.91</td>
    <td align="right">16.53</td>
    <td align="right">21.86</td>
    <td align="right">22.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.63</td>
    <td align="right">41.55</td>
    <td align="right">25.90</td>
    <td align="right">36.82</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.34</td>
    <td align="right">44.30</td>
    <td align="right">26.51</td>
    <td align="right">37.83</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.07</td>
    <td align="right">20.21</td>
    <td align="right">20.89</td>
    <td align="right">24.98</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">19.95</td>
    <td align="right">19.66</td>
    <td align="right">19.65</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.15</td>
    <td align="right">20.23</td>
    <td align="right">20.23</td>
    <td align="right">20.22</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.57</td>
    <td align="right">9.87</td>
    <td align="right">9.87</td>
    <td align="right">9.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">28.16</td>
    <td align="right">28.16</td>
    <td align="right">28.15</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.19</td>
    <td align="right">27.59</td>
    <td align="right">27.60</td>
    <td align="right">27.58</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.94</td>
    <td align="right">15.07</td>
    <td align="right">15.06</td>
    <td align="right">15.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.00</td>
    <td align="right">35.34</td>
    <td align="right">35.29</td>
    <td align="right">35.28</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">34.86</td>
    <td align="right">34.80</td>
    <td align="right">34.97</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.88</td>
    <td align="right">17.88</td>
    <td align="right">17.91</td>
    <td align="right">17.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.60</td>
    <td align="right">38.52</td>
    <td align="right">38.46</td>
    <td align="right">38.49</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.40</td>
    <td align="right">41.87</td>
    <td align="right">41.87</td>
    <td align="right">42.08</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.08</td>
    <td align="right">20.87</td>
    <td align="right">20.86</td>
    <td align="right">20.87</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.34</td>
    <td align="right">9.06</td>
    <td align="right">17.24</td>
    <td align="right">15.67</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">20.46</td>
    <td align="right">23.46</td>
    <td align="right">24.11</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.11</td>
    <td align="right">20.09</td>
    <td align="right">22.97</td>
    <td align="right">24.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.81</td>
    <td align="right">14.36</td>
    <td align="right">20.67</td>
    <td align="right">20.34</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.54</td>
    <td align="right">24.56</td>
    <td align="right">27.94</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.20</td>
    <td align="right">25.86</td>
    <td align="right">24.40</td>
    <td align="right">27.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.28</td>
    <td align="right">15.20</td>
    <td align="right">20.31</td>
    <td align="right">20.63</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.96</td>
    <td align="right">38.75</td>
    <td align="right">26.64</td>
    <td align="right">35.22</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">37.51</td>
    <td align="right">26.28</td>
    <td align="right">34.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.84</td>
    <td align="right">19.84</td>
    <td align="right">20.73</td>
    <td align="right">24.64</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">41.65</td>
    <td align="right">25.85</td>
    <td align="right">36.74</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.29</td>
    <td align="right">44.14</td>
    <td align="right">26.51</td>
    <td align="right">37.80</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.11</td>
    <td align="right">9.87</td>
    <td align="right">9.71</td>
    <td align="right">9.72</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">19.93</td>
    <td align="right">19.93</td>
    <td align="right">19.64</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.13</td>
    <td align="right">20.18</td>
    <td align="right">20.18</td>
    <td align="right">20.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.86</td>
    <td align="right">14.85</td>
    <td align="right">14.83</td>
    <td align="right">14.82</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">28.11</td>
    <td align="right">28.11</td>
    <td align="right">28.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.17</td>
    <td align="right">27.61</td>
    <td align="right">27.61</td>
    <td align="right">27.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.26</td>
    <td align="right">17.53</td>
    <td align="right">17.54</td>
    <td align="right">17.54</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.96</td>
    <td align="right">35.24</td>
    <td align="right">35.26</td>
    <td align="right">35.27</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.52</td>
    <td align="right">35.36</td>
    <td align="right">34.86</td>
    <td align="right">35.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.84</td>
    <td align="right">20.71</td>
    <td align="right">20.71</td>
    <td align="right">20.71</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.62</td>
    <td align="right">38.46</td>
    <td align="right">38.47</td>
    <td align="right">38.43</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.45</td>
    <td align="right">42.20</td>
    <td align="right">41.90</td>
    <td align="right">42.09</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.21</td>
    <td align="right">21.01</td>
    <td align="right">24.02</td>
    <td align="right">24.38</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.59</td>
    <td align="right">42.69</td>
    <td align="right">41.33</td>
    <td align="right">42.22</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.20</td>
    <td align="right">30.33</td>
    <td align="right">29.31</td>
    <td align="right">30.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.03</td>
    <td align="right">30.07</td>
    <td align="right">24.32</td>
    <td align="right">30.08</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.89</td>
    <td align="right">45.99</td>
    <td align="right">39.48</td>
    <td align="right">43.03</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.80</td>
    <td align="right">39.33</td>
    <td align="right">30.04</td>
    <td align="right">35.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.12</td>
    <td align="right">36.14</td>
    <td align="right">24.53</td>
    <td align="right">34.15</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.35</td>
    <td align="right">54.90</td>
    <td align="right">40.15</td>
    <td align="right">47.80</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.36</td>
    <td align="right">45.68</td>
    <td align="right">31.72</td>
    <td align="right">40.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.77</td>
    <td align="right">47.73</td>
    <td align="right">30.30</td>
    <td align="right">42.07</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.87</td>
    <td align="right">59.19</td>
    <td align="right">44.87</td>
    <td align="right">52.45</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.35</td>
    <td align="right">57.73</td>
    <td align="right">33.15</td>
    <td align="right">47.26</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.23</td>
    <td align="right">21.12</td>
    <td align="right">20.93</td>
    <td align="right">21.11</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.68</td>
    <td align="right">39.18</td>
    <td align="right">38.91</td>
    <td align="right">38.95</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.51</td>
    <td align="right">28.16</td>
    <td align="right">27.99</td>
    <td align="right">28.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.03</td>
    <td align="right">27.93</td>
    <td align="right">27.96</td>
    <td align="right">27.92</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.81</td>
    <td align="right">43.28</td>
    <td align="right">43.71</td>
    <td align="right">43.19</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.74</td>
    <td align="right">36.78</td>
    <td align="right">36.61</td>
    <td align="right">36.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.11</td>
    <td align="right">32.94</td>
    <td align="right">32.95</td>
    <td align="right">32.94</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.03</td>
    <td align="right">48.89</td>
    <td align="right">49.06</td>
    <td align="right">49.19</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.64</td>
    <td align="right">38.62</td>
    <td align="right">38.63</td>
    <td align="right">38.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.76</td>
    <td align="right">38.89</td>
    <td align="right">38.83</td>
    <td align="right">38.87</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.14</td>
    <td align="right">53.37</td>
    <td align="right">53.16</td>
    <td align="right">53.36</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.33</td>
    <td align="right">51.63</td>
    <td align="right">51.54</td>
    <td align="right">51.31</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.42</td>
    <td align="right">61.55</td>
    <td align="right">22.77</td>
    <td align="right">52.68</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">27.04</td>
    <td align="right">39.73</td>
    <td align="right">33.04</td>
    <td align="right">37.54</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.28</td>
    <td align="right">17.27</td>
    <td align="right">17.31</td>
    <td align="right">17.25</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.07</td>
    <td align="right">20.03</td>
    <td align="right">20.06</td>
    <td align="right">20.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">80.89</td>
    <td align="right">106.64</td>
    <td align="right">44.95</td>
    <td align="right">76.90</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.48</td>
    <td align="right">26.59</td>
    <td align="right">26.62</td>
    <td align="right">26.59</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.04</td>
    <td align="right">34.18</td>
    <td align="right">34.26</td>
    <td align="right">34.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">143.98</td>
    <td align="right">209.73</td>
    <td align="right">67.93</td>
    <td align="right">142.74</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.27</td>
    <td align="right">48.69</td>
    <td align="right">51.04</td>
    <td align="right">49.43</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.78</td>
    <td align="right">51.64</td>
    <td align="right">51.77</td>
    <td align="right">51.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">268.59</td>
    <td align="right">329.98</td>
    <td align="right">84.17</td>
    <td align="right">207.67</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.26</td>
    <td align="right">64.96</td>
    <td align="right">64.75</td>
    <td align="right">64.86</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.41</td>
    <td align="right">68.79</td>
    <td align="right">68.75</td>
    <td align="right">69.01</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.66</td>
    <td align="right">37.92</td>
    <td align="right">38.24</td>
    <td align="right">37.70</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.67</td>
    <td align="right">16.64</td>
    <td align="right">16.67</td>
    <td align="right">16.68</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.30</td>
    <td align="right">20.42</td>
    <td align="right">20.48</td>
    <td align="right">20.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">70.28</td>
    <td align="right">96.24</td>
    <td align="right">95.98</td>
    <td align="right">96.38</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.38</td>
    <td align="right">27.32</td>
    <td align="right">27.41</td>
    <td align="right">27.34</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.90</td>
    <td align="right">35.43</td>
    <td align="right">35.44</td>
    <td align="right">35.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.39</td>
    <td align="right">188.85</td>
    <td align="right">188.74</td>
    <td align="right">189.32</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.23</td>
    <td align="right">49.25</td>
    <td align="right">49.22</td>
    <td align="right">49.09</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.58</td>
    <td align="right">52.21</td>
    <td align="right">52.41</td>
    <td align="right">52.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">269.88</td>
    <td align="right">293.11</td>
    <td align="right">295.55</td>
    <td align="right">290.98</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.24</td>
    <td align="right">63.31</td>
    <td align="right">63.22</td>
    <td align="right">63.33</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.66</td>
    <td align="right">68.84</td>
    <td align="right">68.86</td>
    <td align="right">68.81</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.13</td>
    <td align="right">23.10</td>
    <td align="right">25.34</td>
    <td align="right">28.08</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.24</td>
    <td align="right">24.47</td>
    <td align="right">25.83</td>
    <td align="right">29.40</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.38</td>
    <td align="right">11.08</td>
    <td align="right">19.90</td>
    <td align="right">18.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.99</td>
    <td align="right">36.84</td>
    <td align="right">31.81</td>
    <td align="right">39.45</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.77</td>
    <td align="right">42.37</td>
    <td align="right">33.15</td>
    <td align="right">42.46</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.61</td>
    <td align="right">21.93</td>
    <td align="right">26.24</td>
    <td align="right">27.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.42</td>
    <td align="right">72.27</td>
    <td align="right">42.78</td>
    <td align="right">65.38</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.72</td>
    <td align="right">73.61</td>
    <td align="right">44.52</td>
    <td align="right">66.81</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.70</td>
    <td align="right">39.66</td>
    <td align="right">34.66</td>
    <td align="right">41.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.24</td>
    <td align="right">91.50</td>
    <td align="right">47.66</td>
    <td align="right">81.48</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.60</td>
    <td align="right">94.68</td>
    <td align="right">49.80</td>
    <td align="right">83.36</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.94</td>
    <td align="right">53.14</td>
    <td align="right">37.70</td>
    <td align="right">53.14</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.23</td>
    <td align="right">23.92</td>
    <td align="right">23.96</td>
    <td align="right">23.89</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.78</td>
    <td align="right">24.38</td>
    <td align="right">24.44</td>
    <td align="right">24.46</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">8.80</td>
    <td align="right">11.27</td>
    <td align="right">11.23</td>
    <td align="right">11.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.87</td>
    <td align="right">43.21</td>
    <td align="right">43.12</td>
    <td align="right">43.11</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.19</td>
    <td align="right">44.59</td>
    <td align="right">44.71</td>
    <td align="right">44.77</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.45</td>
    <td align="right">26.34</td>
    <td align="right">25.97</td>
    <td align="right">25.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.96</td>
    <td align="right">67.44</td>
    <td align="right">67.46</td>
    <td align="right">67.49</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.88</td>
    <td align="right">69.38</td>
    <td align="right">69.42</td>
    <td align="right">69.47</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.93</td>
    <td align="right">40.62</td>
    <td align="right">40.76</td>
    <td align="right">40.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.73</td>
    <td align="right">87.23</td>
    <td align="right">87.21</td>
    <td align="right">87.14</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.22</td>
    <td align="right">94.78</td>
    <td align="right">94.85</td>
    <td align="right">94.97</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.14</td>
    <td align="right">53.36</td>
    <td align="right">53.31</td>
    <td align="right">53.37</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.92</td>
    <td align="right">12.12</td>
    <td align="right">20.02</td>
    <td align="right">18.37</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.12</td>
    <td align="right">24.29</td>
    <td align="right">25.86</td>
    <td align="right">29.21</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.06</td>
    <td align="right">24.34</td>
    <td align="right">25.60</td>
    <td align="right">29.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.17</td>
    <td align="right">25.31</td>
    <td align="right">27.60</td>
    <td align="right">30.00</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.72</td>
    <td align="right">34.35</td>
    <td align="right">29.90</td>
    <td align="right">36.68</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.92</td>
    <td align="right">42.59</td>
    <td align="right">33.21</td>
    <td align="right">43.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.67</td>
    <td align="right">38.58</td>
    <td align="right">33.12</td>
    <td align="right">39.62</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.34</td>
    <td align="right">71.48</td>
    <td align="right">43.68</td>
    <td align="right">65.33</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.61</td>
    <td align="right">71.95</td>
    <td align="right">43.62</td>
    <td align="right">65.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.17</td>
    <td align="right">52.69</td>
    <td align="right">37.78</td>
    <td align="right">53.02</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.49</td>
    <td align="right">92.13</td>
    <td align="right">47.93</td>
    <td align="right">82.13</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.59</td>
    <td align="right">94.94</td>
    <td align="right">49.85</td>
    <td align="right">83.65</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.48</td>
    <td align="right">12.56</td>
    <td align="right">12.38</td>
    <td align="right">12.81</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.17</td>
    <td align="right">24.16</td>
    <td align="right">24.13</td>
    <td align="right">23.99</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.31</td>
    <td align="right">24.00</td>
    <td align="right">24.00</td>
    <td align="right">23.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.50</td>
    <td align="right">26.42</td>
    <td align="right">26.41</td>
    <td align="right">26.47</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.57</td>
    <td align="right">39.08</td>
    <td align="right">39.10</td>
    <td align="right">39.10</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.47</td>
    <td align="right">45.22</td>
    <td align="right">45.10</td>
    <td align="right">45.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.84</td>
    <td align="right">40.71</td>
    <td align="right">40.70</td>
    <td align="right">40.71</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.04</td>
    <td align="right">68.99</td>
    <td align="right">68.97</td>
    <td align="right">68.99</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.47</td>
    <td align="right">69.61</td>
    <td align="right">69.53</td>
    <td align="right">69.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.20</td>
    <td align="right">53.62</td>
    <td align="right">53.61</td>
    <td align="right">53.63</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.06</td>
    <td align="right">88.79</td>
    <td align="right">88.82</td>
    <td align="right">88.82</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.87</td>
    <td align="right">94.93</td>
    <td align="right">94.88</td>
    <td align="right">94.98</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.96</td>
    <td align="right">24.35</td>
    <td align="right">26.07</td>
    <td align="right">29.13</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.24</td>
    <td align="right">43.20</td>
    <td align="right">42.08</td>
    <td align="right">42.85</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">32.57</td>
    <td align="right">35.68</td>
    <td align="right">32.50</td>
    <td align="right">35.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.01</td>
    <td align="right">43.58</td>
    <td align="right">31.65</td>
    <td align="right">43.79</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">63.85</td>
    <td align="right">58.52</td>
    <td align="right">49.35</td>
    <td align="right">55.51</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.01</td>
    <td align="right">59.72</td>
    <td align="right">37.68</td>
    <td align="right">52.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.77</td>
    <td align="right">63.31</td>
    <td align="right">40.38</td>
    <td align="right">61.05</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.79</td>
    <td align="right">88.03</td>
    <td align="right">63.16</td>
    <td align="right">79.70</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.41</td>
    <td align="right">92.06</td>
    <td align="right">43.54</td>
    <td align="right">75.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.29</td>
    <td align="right">89.97</td>
    <td align="right">61.28</td>
    <td align="right">89.23</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">111.48</td>
    <td align="right">105.70</td>
    <td align="right">78.81</td>
    <td align="right">96.06</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.85</td>
    <td align="right">133.15</td>
    <td align="right">51.00</td>
    <td align="right">104.98</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">23.17</td>
    <td align="right">27.18</td>
    <td align="right">27.20</td>
    <td align="right">27.19</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.24</td>
    <td align="right">40.22</td>
    <td align="right">40.05</td>
    <td align="right">40.07</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.44</td>
    <td align="right">33.99</td>
    <td align="right">34.05</td>
    <td align="right">34.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.13</td>
    <td align="right">41.18</td>
    <td align="right">41.14</td>
    <td align="right">41.16</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.11</td>
    <td align="right">54.63</td>
    <td align="right">56.53</td>
    <td align="right">54.63</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.97</td>
    <td align="right">57.60</td>
    <td align="right">57.67</td>
    <td align="right">57.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.02</td>
    <td align="right">61.34</td>
    <td align="right">61.33</td>
    <td align="right">61.32</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.81</td>
    <td align="right">80.73</td>
    <td align="right">80.92</td>
    <td align="right">80.96</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.89</td>
    <td align="right">82.99</td>
    <td align="right">83.02</td>
    <td align="right">82.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.81</td>
    <td align="right">80.68</td>
    <td align="right">80.64</td>
    <td align="right">80.65</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.56</td>
    <td align="right">99.32</td>
    <td align="right">99.23</td>
    <td align="right">104.57</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.36</td>
    <td align="right">120.98</td>
    <td align="right">121.00</td>
    <td align="right">120.86</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.75</td>
    <td align="right">7.08</td>
    <td align="right">5.35</td>
    <td align="right">12.32</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">67.20</td>
    <td align="right">62.53</td>
    <td align="right">42.72</td>
    <td align="right">52.18</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.07</td>
    <td align="right">21.51</td>
    <td align="right">23.96</td>
    <td align="right">26.46</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.07</td>
    <td align="right">25.06</td>
    <td align="right">26.08</td>
    <td align="right">28.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.73</td>
    <td align="right">92.22</td>
    <td align="right">46.18</td>
    <td align="right">69.39</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.84</td>
    <td align="right">23.04</td>
    <td align="right">25.13</td>
    <td align="right">29.11</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.82</td>
    <td align="right">27.17</td>
    <td align="right">28.45</td>
    <td align="right">30.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">121.92</td>
    <td align="right">112.96</td>
    <td align="right">44.93</td>
    <td align="right">78.45</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">26.09</td>
    <td align="right">37.17</td>
    <td align="right">37.93</td>
    <td align="right">43.22</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.42</td>
    <td align="right">31.98</td>
    <td align="right">31.53</td>
    <td align="right">38.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">157.83</td>
    <td align="right">149.28</td>
    <td align="right">45.86</td>
    <td align="right">96.82</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">29.88</td>
    <td align="right">27.11</td>
    <td align="right">27.63</td>
    <td align="right">33.79</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.15</td>
    <td align="right">32.67</td>
    <td align="right">32.66</td>
    <td align="right">36.41</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.48</td>
    <td align="right">66.07</td>
    <td align="right">66.30</td>
    <td align="right">69.55</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.10</td>
    <td align="right">21.65</td>
    <td align="right">24.77</td>
    <td align="right">26.69</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.04</td>
    <td align="right">24.77</td>
    <td align="right">26.21</td>
    <td align="right">28.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">100.04</td>
    <td align="right">101.03</td>
    <td align="right">100.05</td>
    <td align="right">103.58</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.79</td>
    <td align="right">23.02</td>
    <td align="right">24.92</td>
    <td align="right">28.46</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.67</td>
    <td align="right">27.60</td>
    <td align="right">28.47</td>
    <td align="right">30.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">124.51</td>
    <td align="right">128.16</td>
    <td align="right">121.76</td>
    <td align="right">127.06</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">26.06</td>
    <td align="right">25.78</td>
    <td align="right">26.71</td>
    <td align="right">31.38</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.44</td>
    <td align="right">35.04</td>
    <td align="right">34.56</td>
    <td align="right">37.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">157.17</td>
    <td align="right">162.92</td>
    <td align="right">160.99</td>
    <td align="right">166.76</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.95</td>
    <td align="right">27.11</td>
    <td align="right">27.62</td>
    <td align="right">33.74</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">37.86</td>
    <td align="right">31.83</td>
    <td align="right">31.40</td>
    <td align="right">35.15</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.30</td>
    <td align="right">43.38</td>
    <td align="right">34.11</td>
    <td align="right">38.80</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.47</td>
    <td align="right">43.00</td>
    <td align="right">34.95</td>
    <td align="right">39.44</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.42</td>
    <td align="right">28.01</td>
    <td align="right">28.06</td>
    <td align="right">32.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.62</td>
    <td align="right">58.73</td>
    <td align="right">34.73</td>
    <td align="right">47.01</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.37</td>
    <td align="right">58.93</td>
    <td align="right">36.67</td>
    <td align="right">48.38</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.85</td>
    <td align="right">37.58</td>
    <td align="right">27.79</td>
    <td align="right">37.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">39.50</td>
    <td align="right">77.81</td>
    <td align="right">35.61</td>
    <td align="right">57.04</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.91</td>
    <td align="right">77.92</td>
    <td align="right">37.57</td>
    <td align="right">58.05</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">28.00</td>
    <td align="right">49.49</td>
    <td align="right">32.40</td>
    <td align="right">45.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.76</td>
    <td align="right">87.62</td>
    <td align="right">34.86</td>
    <td align="right">62.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">53.05</td>
    <td align="right">95.76</td>
    <td align="right">38.05</td>
    <td align="right">67.31</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.13</td>
    <td align="right">48.97</td>
    <td align="right">32.08</td>
    <td align="right">44.89</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.21</td>
    <td align="right">40.89</td>
    <td align="right">41.03</td>
    <td align="right">43.65</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.28</td>
    <td align="right">40.88</td>
    <td align="right">41.50</td>
    <td align="right">44.07</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.36</td>
    <td align="right">29.45</td>
    <td align="right">29.66</td>
    <td align="right">33.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.67</td>
    <td align="right">57.29</td>
    <td align="right">55.83</td>
    <td align="right">58.94</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.34</td>
    <td align="right">56.45</td>
    <td align="right">56.33</td>
    <td align="right">59.24</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.88</td>
    <td align="right">37.24</td>
    <td align="right">36.98</td>
    <td align="right">37.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">39.34</td>
    <td align="right">76.80</td>
    <td align="right">75.47</td>
    <td align="right">78.91</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.42</td>
    <td align="right">80.70</td>
    <td align="right">81.11</td>
    <td align="right">88.65</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.23</td>
    <td align="right">50.52</td>
    <td align="right">50.46</td>
    <td align="right">54.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">43.63</td>
    <td align="right">86.09</td>
    <td align="right">84.49</td>
    <td align="right">87.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.31</td>
    <td align="right">88.57</td>
    <td align="right">88.92</td>
    <td align="right">91.98</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">31.90</td>
    <td align="right">49.19</td>
    <td align="right">48.96</td>
    <td align="right">53.08</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.83</td>
    <td align="right">27.13</td>
    <td align="right">27.16</td>
    <td align="right">31.69</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.78</td>
    <td align="right">29.19</td>
    <td align="right">29.23</td>
    <td align="right">33.86</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.39</td>
    <td align="right">29.16</td>
    <td align="right">29.23</td>
    <td align="right">33.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.89</td>
    <td align="right">39.74</td>
    <td align="right">29.26</td>
    <td align="right">39.46</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.71</td>
    <td align="right">39.12</td>
    <td align="right">29.71</td>
    <td align="right">39.23</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.90</td>
    <td align="right">41.54</td>
    <td align="right">31.50</td>
    <td align="right">41.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.18</td>
    <td align="right">56.00</td>
    <td align="right">39.07</td>
    <td align="right">52.73</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.66</td>
    <td align="right">52.10</td>
    <td align="right">34.50</td>
    <td align="right">47.73</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.34</td>
    <td align="right">49.88</td>
    <td align="right">32.72</td>
    <td align="right">45.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">29.60</td>
    <td align="right">47.06</td>
    <td align="right">30.37</td>
    <td align="right">43.38</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">42.41</td>
    <td align="right">52.36</td>
    <td align="right">33.14</td>
    <td align="right">47.28</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">42.70</td>
    <td align="right">51.56</td>
    <td align="right">32.35</td>
    <td align="right">46.49</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.84</td>
    <td align="right">29.32</td>
    <td align="right">29.40</td>
    <td align="right">33.29</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.82</td>
    <td align="right">29.51</td>
    <td align="right">29.24</td>
    <td align="right">33.72</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.38</td>
    <td align="right">29.39</td>
    <td align="right">29.39</td>
    <td align="right">34.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.86</td>
    <td align="right">38.42</td>
    <td align="right">38.25</td>
    <td align="right">38.71</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.74</td>
    <td align="right">37.88</td>
    <td align="right">37.78</td>
    <td align="right">38.45</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.82</td>
    <td align="right">39.30</td>
    <td align="right">38.95</td>
    <td align="right">40.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">29.47</td>
    <td align="right">48.60</td>
    <td align="right">48.36</td>
    <td align="right">52.14</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.84</td>
    <td align="right">51.33</td>
    <td align="right">51.03</td>
    <td align="right">54.98</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.69</td>
    <td align="right">50.99</td>
    <td align="right">50.92</td>
    <td align="right">54.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">29.84</td>
    <td align="right">48.88</td>
    <td align="right">48.82</td>
    <td align="right">52.72</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">34.95</td>
    <td align="right">53.12</td>
    <td align="right">52.96</td>
    <td align="right">56.73</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.01</td>
    <td align="right">53.02</td>
    <td align="right">52.76</td>
    <td align="right">56.46</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">28.23</td>
    <td align="right">44.46</td>
    <td align="right">34.28</td>
    <td align="right">40.19</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.97</td>
    <td align="right">56.06</td>
    <td align="right">38.50</td>
    <td align="right">47.30</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.55</td>
    <td align="right">63.89</td>
    <td align="right">39.50</td>
    <td align="right">52.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">37.88</td>
    <td align="right">62.06</td>
    <td align="right">35.63</td>
    <td align="right">50.07</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.02</td>
    <td align="right">62.11</td>
    <td align="right">36.28</td>
    <td align="right">50.41</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.36</td>
    <td align="right">83.72</td>
    <td align="right">39.60</td>
    <td align="right">61.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">44.19</td>
    <td align="right">74.29</td>
    <td align="right">37.82</td>
    <td align="right">59.56</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.02</td>
    <td align="right">79.79</td>
    <td align="right">37.29</td>
    <td align="right">60.53</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">50.80</td>
    <td align="right">88.81</td>
    <td align="right">37.77</td>
    <td align="right">65.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.55</td>
    <td align="right">99.23</td>
    <td align="right">36.34</td>
    <td align="right">69.10</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.87</td>
    <td align="right">99.01</td>
    <td align="right">36.47</td>
    <td align="right">70.11</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">66.11</td>
    <td align="right">121.42</td>
    <td align="right">39.16</td>
    <td align="right">81.12</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">28.33</td>
    <td align="right">42.43</td>
    <td align="right">42.48</td>
    <td align="right">45.17</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.75</td>
    <td align="right">47.70</td>
    <td align="right">48.04</td>
    <td align="right">50.65</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.44</td>
    <td align="right">60.38</td>
    <td align="right">61.22</td>
    <td align="right">63.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">38.05</td>
    <td align="right">56.39</td>
    <td align="right">56.81</td>
    <td align="right">59.44</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.08</td>
    <td align="right">59.34</td>
    <td align="right">60.73</td>
    <td align="right">62.19</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.39</td>
    <td align="right">78.20</td>
    <td align="right">77.49</td>
    <td align="right">80.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.20</td>
    <td align="right">68.21</td>
    <td align="right">68.13</td>
    <td align="right">71.80</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.27</td>
    <td align="right">77.38</td>
    <td align="right">76.85</td>
    <td align="right">79.51</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.44</td>
    <td align="right">83.50</td>
    <td align="right">83.43</td>
    <td align="right">86.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">57.91</td>
    <td align="right">90.14</td>
    <td align="right">90.39</td>
    <td align="right">95.60</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">57.06</td>
    <td align="right">91.32</td>
    <td align="right">92.94</td>
    <td align="right">96.06</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">65.67</td>
    <td align="right">119.70</td>
    <td align="right">119.68</td>
    <td align="right">124.15</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">65.29</td>
    <td align="right">34.28</td>
    <td align="right">21.01</td>
    <td align="right">38.04</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">102.58</td>
    <td align="right">130.37</td>
    <td align="right">71.60</td>
    <td align="right">100.68</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">24.28</td>
    <td align="right">24.85</td>
    <td align="right">27.76</td>
    <td align="right">31.01</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">34.75</td>
    <td align="right">29.35</td>
    <td align="right">30.42</td>
    <td align="right">32.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">188.61</td>
    <td align="right">220.51</td>
    <td align="right">82.99</td>
    <td align="right">151.01</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">31.91</td>
    <td align="right">27.02</td>
    <td align="right">29.03</td>
    <td align="right">33.91</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">34.07</td>
    <td align="right">30.98</td>
    <td align="right">31.92</td>
    <td align="right">34.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">278.82</td>
    <td align="right">276.15</td>
    <td align="right">81.59</td>
    <td align="right">177.07</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.46</td>
    <td align="right">41.41</td>
    <td align="right">42.39</td>
    <td align="right">48.72</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">65.27</td>
    <td align="right">65.75</td>
    <td align="right">65.38</td>
    <td align="right">67.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">512.54</td>
    <td align="right">495.64</td>
    <td align="right">111.54</td>
    <td align="right">300.33</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">54.39</td>
    <td align="right">54.34</td>
    <td align="right">54.88</td>
    <td align="right">61.96</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.93</td>
    <td align="right">62.89</td>
    <td align="right">61.68</td>
    <td align="right">64.84</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">101.57</td>
    <td align="right">88.41</td>
    <td align="right">88.51</td>
    <td align="right">94.27</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">25.73</td>
    <td align="right">22.06</td>
    <td align="right">25.71</td>
    <td align="right">28.29</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">31.11</td>
    <td align="right">26.78</td>
    <td align="right">27.98</td>
    <td align="right">29.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">186.21</td>
    <td align="right">235.20</td>
    <td align="right">235.50</td>
    <td align="right">240.29</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.12</td>
    <td align="right">30.57</td>
    <td align="right">32.43</td>
    <td align="right">36.83</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">33.54</td>
    <td align="right">46.08</td>
    <td align="right">47.06</td>
    <td align="right">48.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">410.87</td>
    <td align="right">403.81</td>
    <td align="right">401.02</td>
    <td align="right">406.56</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">59.84</td>
    <td align="right">59.75</td>
    <td align="right">60.48</td>
    <td align="right">65.90</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">50.73</td>
    <td align="right">52.74</td>
    <td align="right">51.33</td>
    <td align="right">53.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">445.42</td>
    <td align="right">436.46</td>
    <td align="right">436.39</td>
    <td align="right">443.02</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">61.59</td>
    <td align="right">61.49</td>
    <td align="right">62.25</td>
    <td align="right">68.09</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.81</td>
    <td align="right">62.10</td>
    <td align="right">61.29</td>
    <td align="right">64.35</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">48.66</td>
    <td align="right">81.62</td>
    <td align="right">77.93</td>
    <td align="right">81.17</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">36.94</td>
    <td align="right">57.92</td>
    <td align="right">53.93</td>
    <td align="right">56.40</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">21.32</td>
    <td align="right">33.69</td>
    <td align="right">33.78</td>
    <td align="right">38.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.69</td>
    <td align="right">61.31</td>
    <td align="right">38.64</td>
    <td align="right">51.15</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">46.99</td>
    <td align="right">77.44</td>
    <td align="right">61.01</td>
    <td align="right">69.62</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.01</td>
    <td align="right">40.19</td>
    <td align="right">30.43</td>
    <td align="right">40.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">63.89</td>
    <td align="right">94.14</td>
    <td align="right">55.38</td>
    <td align="right">75.76</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">67.05</td>
    <td align="right">97.24</td>
    <td align="right">61.45</td>
    <td align="right">79.57</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">49.75</td>
    <td align="right">72.41</td>
    <td align="right">55.96</td>
    <td align="right">68.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">77.73</td>
    <td align="right">112.39</td>
    <td align="right">62.31</td>
    <td align="right">88.36</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.42</td>
    <td align="right">126.27</td>
    <td align="right">74.01</td>
    <td align="right">100.55</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">60.20</td>
    <td align="right">84.86</td>
    <td align="right">67.83</td>
    <td align="right">80.81</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">33.64</td>
    <td align="right">41.33</td>
    <td align="right">41.77</td>
    <td align="right">43.95</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.12</td>
    <td align="right">41.76</td>
    <td align="right">41.87</td>
    <td align="right">44.73</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">19.17</td>
    <td align="right">30.89</td>
    <td align="right">31.07</td>
    <td align="right">35.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.36</td>
    <td align="right">59.15</td>
    <td align="right">57.98</td>
    <td align="right">60.78</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">67.97</td>
    <td align="right">80.83</td>
    <td align="right">80.80</td>
    <td align="right">83.83</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">25.05</td>
    <td align="right">46.89</td>
    <td align="right">48.80</td>
    <td align="right">49.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">63.87</td>
    <td align="right">92.74</td>
    <td align="right">91.63</td>
    <td align="right">94.79</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">67.20</td>
    <td align="right">96.37</td>
    <td align="right">96.14</td>
    <td align="right">99.14</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">50.58</td>
    <td align="right">73.97</td>
    <td align="right">73.44</td>
    <td align="right">77.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">76.92</td>
    <td align="right">109.33</td>
    <td align="right">107.75</td>
    <td align="right">111.35</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.24</td>
    <td align="right">116.87</td>
    <td align="right">117.48</td>
    <td align="right">120.07</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">67.28</td>
    <td align="right">92.61</td>
    <td align="right">92.23</td>
    <td align="right">96.64</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">23.35</td>
    <td align="right">28.70</td>
    <td align="right">28.81</td>
    <td align="right">33.67</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">24.06</td>
    <td align="right">34.63</td>
    <td align="right">34.92</td>
    <td align="right">39.77</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.78</td>
    <td align="right">30.40</td>
    <td align="right">30.44</td>
    <td align="right">34.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">23.46</td>
    <td align="right">63.41</td>
    <td align="right">53.67</td>
    <td align="right">63.64</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">23.86</td>
    <td align="right">43.87</td>
    <td align="right">34.12</td>
    <td align="right">43.67</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">29.05</td>
    <td align="right">44.34</td>
    <td align="right">34.78</td>
    <td align="right">45.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">51.21</td>
    <td align="right">72.68</td>
    <td align="right">56.50</td>
    <td align="right">69.27</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.01</td>
    <td align="right">73.06</td>
    <td align="right">54.82</td>
    <td align="right">68.50</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">54.11</td>
    <td align="right">74.67</td>
    <td align="right">57.54</td>
    <td align="right">70.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">68.67</td>
    <td align="right">92.48</td>
    <td align="right">75.70</td>
    <td align="right">88.73</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">65.01</td>
    <td align="right">88.11</td>
    <td align="right">68.94</td>
    <td align="right">82.92</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.70</td>
    <td align="right">89.47</td>
    <td align="right">70.17</td>
    <td align="right">84.23</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">19.87</td>
    <td align="right">30.54</td>
    <td align="right">30.68</td>
    <td align="right">34.81</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">25.26</td>
    <td align="right">53.86</td>
    <td align="right">53.74</td>
    <td align="right">58.55</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">25.03</td>
    <td align="right">35.79</td>
    <td align="right">35.81</td>
    <td align="right">40.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">24.51</td>
    <td align="right">42.58</td>
    <td align="right">42.02</td>
    <td align="right">42.97</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.44</td>
    <td align="right">40.87</td>
    <td align="right">40.66</td>
    <td align="right">41.75</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">25.91</td>
    <td align="right">43.51</td>
    <td align="right">42.69</td>
    <td align="right">44.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.77</td>
    <td align="right">72.82</td>
    <td align="right">72.87</td>
    <td align="right">77.33</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.16</td>
    <td align="right">75.09</td>
    <td align="right">74.81</td>
    <td align="right">78.68</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.88</td>
    <td align="right">78.03</td>
    <td align="right">78.19</td>
    <td align="right">82.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.93</td>
    <td align="right">86.91</td>
    <td align="right">86.85</td>
    <td align="right">90.62</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">65.25</td>
    <td align="right">90.46</td>
    <td align="right">90.69</td>
    <td align="right">94.55</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.61</td>
    <td align="right">93.42</td>
    <td align="right">93.85</td>
    <td align="right">97.45</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">31.77</td>
    <td align="right">44.92</td>
    <td align="right">36.37</td>
    <td align="right">41.74</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.88</td>
    <td align="right">56.41</td>
    <td align="right">41.44</td>
    <td align="right">48.36</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">64.96</td>
    <td align="right">71.28</td>
    <td align="right">46.30</td>
    <td align="right">59.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">50.74</td>
    <td align="right">65.45</td>
    <td align="right">40.67</td>
    <td align="right">54.01</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">51.87</td>
    <td align="right">63.64</td>
    <td align="right">40.27</td>
    <td align="right">53.14</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.92</td>
    <td align="right">86.78</td>
    <td align="right">42.60</td>
    <td align="right">65.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.22</td>
    <td align="right">87.52</td>
    <td align="right">53.31</td>
    <td align="right">71.70</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">73.48</td>
    <td align="right">98.13</td>
    <td align="right">61.75</td>
    <td align="right">82.46</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">77.96</td>
    <td align="right">116.16</td>
    <td align="right">49.42</td>
    <td align="right">86.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.26</td>
    <td align="right">122.99</td>
    <td align="right">65.34</td>
    <td align="right">95.92</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">101.33</td>
    <td align="right">136.80</td>
    <td align="right">79.67</td>
    <td align="right">110.39</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">117.14</td>
    <td align="right">160.70</td>
    <td align="right">53.29</td>
    <td align="right">113.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">38.01</td>
    <td align="right">51.83</td>
    <td align="right">51.90</td>
    <td align="right">55.27</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">44.42</td>
    <td align="right">63.85</td>
    <td align="right">63.96</td>
    <td align="right">66.36</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">52.12</td>
    <td align="right">77.35</td>
    <td align="right">78.09</td>
    <td align="right">80.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">52.12</td>
    <td align="right">60.77</td>
    <td align="right">61.04</td>
    <td align="right">63.85</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">54.20</td>
    <td align="right">84.51</td>
    <td align="right">85.23</td>
    <td align="right">87.85</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">61.97</td>
    <td align="right">80.06</td>
    <td align="right">79.44</td>
    <td align="right">82.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">63.08</td>
    <td align="right">80.73</td>
    <td align="right">80.46</td>
    <td align="right">84.30</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">92.58</td>
    <td align="right">121.74</td>
    <td align="right">121.38</td>
    <td align="right">124.18</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">78.37</td>
    <td align="right">104.80</td>
    <td align="right">106.28</td>
    <td align="right">108.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.98</td>
    <td align="right">111.79</td>
    <td align="right">112.45</td>
    <td align="right">117.18</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.32</td>
    <td align="right">125.24</td>
    <td align="right">125.86</td>
    <td align="right">130.38</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">116.51</td>
    <td align="right">151.86</td>
    <td align="right">152.34</td>
    <td align="right">156.59</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
