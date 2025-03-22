# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.99</td>
    <td align="right">4.47</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.08</td>
    <td align="right">10.58</td>
    <td align="right">16.51</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.95</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.05</td>
    <td align="right">5.72</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.78</td>
    <td align="right">15.53</td>
    <td align="right">17.67</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.81</td>
    <td align="right">4.94</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.98</td>
    <td align="right">8.79</td>
    <td align="right">8.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.59</td>
    <td align="right">18.70</td>
    <td align="right">16.64</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.35</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.15</td>
    <td align="right">13.70</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.41</td>
    <td align="right">22.11</td>
    <td align="right">15.99</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.40</td>
    <td align="right">6.06</td>
    <td align="right">5.90</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">11.43</td>
    <td align="right">15.55</td>
    <td align="right">15.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.94</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.82</td>
    <td align="right">5.03</td>
    <td align="right">5.03</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.48</td>
    <td align="right">6.61</td>
    <td align="right">6.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.11</td>
    <td align="right">3.10</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.40</td>
    <td align="right">5.48</td>
    <td align="right">5.49</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.06</td>
    <td align="right">10.02</td>
    <td align="right">9.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.71</td>
    <td align="right">5.73</td>
    <td align="right">3.89</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.22</td>
    <td align="right">6.27</td>
    <td align="right">6.29</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.72</td>
    <td align="right">14.11</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.66</td>
    <td align="right">5.72</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.68</td>
    <td align="right">6.54</td>
    <td align="right">6.54</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.83</td>
    <td align="right">17.21</td>
    <td align="right">17.21</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">29.93</td>
    <td align="right">17.52</td>
    <td align="right">6.39</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.88</td>
    <td align="right">12.05</td>
    <td align="right">17.22</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.43</td>
    <td align="right">4.71</td>
    <td align="right">4.73</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.79</td>
    <td align="right">6.58</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.37</td>
    <td align="right">17.56</td>
    <td align="right">17.69</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.16</td>
    <td align="right">5.59</td>
    <td align="right">5.54</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.61</td>
    <td align="right">9.37</td>
    <td align="right">9.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.79</td>
    <td align="right">23.25</td>
    <td align="right">17.40</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.42</td>
    <td align="right">6.08</td>
    <td align="right">6.14</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.65</td>
    <td align="right">14.60</td>
    <td align="right">14.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">37.13</td>
    <td align="right">35.52</td>
    <td align="right">18.00</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.00</td>
    <td align="right">8.41</td>
    <td align="right">8.13</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">13.97</td>
    <td align="right">18.09</td>
    <td align="right">17.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.42</td>
    <td align="right">3.86</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.53</td>
    <td align="right">5.71</td>
    <td align="right">5.72</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.27</td>
    <td align="right">7.63</td>
    <td align="right">7.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.73</td>
    <td align="right">3.45</td>
    <td align="right">3.38</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.85</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.67</td>
    <td align="right">10.56</td>
    <td align="right">10.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.15</td>
    <td align="right">6.83</td>
    <td align="right">4.77</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.22</td>
    <td align="right">7.25</td>
    <td align="right">8.01</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.70</td>
    <td align="right">15.40</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">8.13</td>
    <td align="right">7.84</td>
    <td align="right">5.80</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.93</td>
    <td align="right">8.43</td>
    <td align="right">8.98</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.33</td>
    <td align="right">19.88</td>
    <td align="right">20.35</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.64</td>
    <td align="right">4.17</td>
    <td align="right">3.47</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.70</td>
    <td align="right">8.22</td>
    <td align="right">14.66</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.16</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.87</td>
    <td align="right">3.37</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.43</td>
    <td align="right">12.48</td>
    <td align="right">15.83</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.65</td>
    <td align="right">4.32</td>
    <td align="right">4.48</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.51</td>
    <td align="right">3.16</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.37</td>
    <td align="right">15.04</td>
    <td align="right">14.79</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.13</td>
    <td align="right">4.85</td>
    <td align="right">5.03</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.18</td>
    <td align="right">5.69</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.76</td>
    <td align="right">19.12</td>
    <td align="right">15.44</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.75</td>
    <td align="right">5.66</td>
    <td align="right">5.68</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.44</td>
    <td align="right">6.55</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.43</td>
    <td align="right">2.33</td>
    <td align="right">2.33</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.72</td>
    <td align="right">4.32</td>
    <td align="right">4.33</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.95</td>
    <td align="right">3.23</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.98</td>
    <td align="right">2.10</td>
    <td align="right">2.11</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.28</td>
    <td align="right">5.26</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.43</td>
    <td align="right">3.53</td>
    <td align="right">3.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.92</td>
    <td align="right">4.09</td>
    <td align="right">2.96</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.84</td>
    <td align="right">5.94</td>
    <td align="right">6.03</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.39</td>
    <td align="right">5.68</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.86</td>
    <td align="right">4.13</td>
    <td align="right">2.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.64</td>
    <td align="right">3.04</td>
    <td align="right">3.03</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.90</td>
    <td align="right">6.57</td>
    <td align="right">6.52</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.46</td>
    <td align="right">16.85</td>
    <td align="right">6.99</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.26</td>
    <td align="right">10.94</td>
    <td align="right">16.65</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.06</td>
    <td align="right">4.74</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.78</td>
    <td align="right">4.44</td>
    <td align="right">4.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.81</td>
    <td align="right">16.57</td>
    <td align="right">17.72</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.06</td>
    <td align="right">5.79</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.35</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">23.78</td>
    <td align="right">25.43</td>
    <td align="right">17.30</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.75</td>
    <td align="right">7.39</td>
    <td align="right">7.45</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.30</td>
    <td align="right">8.64</td>
    <td align="right">8.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">43.65</td>
    <td align="right">47.55</td>
    <td align="right">20.26</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.61</td>
    <td align="right">11.41</td>
    <td align="right">11.30</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">10.51</td>
    <td align="right">12.85</td>
    <td align="right">13.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.13</td>
    <td align="right">3.12</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.68</td>
    <td align="right">5.51</td>
    <td align="right">5.46</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.83</td>
    <td align="right">4.37</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.87</td>
    <td align="right">3.36</td>
    <td align="right">3.03</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.10</td>
    <td align="right">7.13</td>
    <td align="right">6.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.81</td>
    <td align="right">5.30</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.85</td>
    <td align="right">7.43</td>
    <td align="right">5.51</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.36</td>
    <td align="right">9.24</td>
    <td align="right">8.81</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">8.15</td>
    <td align="right">9.52</td>
    <td align="right">9.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">8.80</td>
    <td align="right">9.64</td>
    <td align="right">6.97</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">6.68</td>
    <td align="right">7.85</td>
    <td align="right">7.26</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">10.97</td>
    <td align="right">13.98</td>
    <td align="right">13.33</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">22.30</td>
    <td align="right">4.41</td>
    <td align="right">3.27</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.34</td>
    <td align="right">5.01</td>
    <td align="right">12.47</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.38</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.38</td>
    <td align="right">1.85</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.67</td>
    <td align="right">7.59</td>
    <td align="right">13.20</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.55</td>
    <td align="right">1.44</td>
    <td align="right">1.40</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.23</td>
    <td align="right">2.06</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.93</td>
    <td align="right">9.44</td>
    <td align="right">11.77</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.86</td>
    <td align="right">1.68</td>
    <td align="right">1.66</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.53</td>
    <td align="right">3.20</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">16.29</td>
    <td align="right">10.68</td>
    <td align="right">11.27</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.05</td>
    <td align="right">2.11</td>
    <td align="right">1.90</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">4.50</td>
    <td align="right">3.76</td>
    <td align="right">3.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.18</td>
    <td align="right">1.89</td>
    <td align="right">1.76</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.61</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.66</td>
    <td align="right">1.98</td>
    <td align="right">1.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.50</td>
    <td align="right">1.36</td>
    <td align="right">1.49</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.81</td>
    <td align="right">1.57</td>
    <td align="right">1.56</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.09</td>
    <td align="right">2.37</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.46</td>
    <td align="right">2.67</td>
    <td align="right">1.92</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.84</td>
    <td align="right">1.83</td>
    <td align="right">1.76</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.04</td>
    <td align="right">2.96</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.20</td>
    <td align="right">3.18</td>
    <td align="right">1.95</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.81</td>
    <td align="right">1.75</td>
    <td align="right">1.68</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.22</td>
    <td align="right">4.26</td>
    <td align="right">4.26</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">28.20</td>
    <td align="right">13.26</td>
    <td align="right">6.18</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.66</td>
    <td align="right">9.63</td>
    <td align="right">18.97</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.04</td>
    <td align="right">4.86</td>
    <td align="right">3.83</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.69</td>
    <td align="right">2.78</td>
    <td align="right">3.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">26.96</td>
    <td align="right">21.68</td>
    <td align="right">22.29</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.42</td>
    <td align="right">6.24</td>
    <td align="right">6.39</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.09</td>
    <td align="right">8.63</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">47.85</td>
    <td align="right">35.03</td>
    <td align="right">22.25</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">8.17</td>
    <td align="right">7.46</td>
    <td align="right">5.99</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.34</td>
    <td align="right">13.74</td>
    <td align="right">13.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">67.48</td>
    <td align="right">53.71</td>
    <td align="right">25.57</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.02</td>
    <td align="right">10.04</td>
    <td align="right">10.74</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">19.84</td>
    <td align="right">18.69</td>
    <td align="right">17.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.09</td>
    <td align="right">3.88</td>
    <td align="right">3.13</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.99</td>
    <td align="right">3.19</td>
    <td align="right">3.20</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.62</td>
    <td align="right">4.37</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.66</td>
    <td align="right">6.79</td>
    <td align="right">6.80</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.33</td>
    <td align="right">5.66</td>
    <td align="right">5.59</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.69</td>
    <td align="right">8.18</td>
    <td align="right">9.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.08</td>
    <td align="right">12.05</td>
    <td align="right">6.42</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.79</td>
    <td align="right">8.00</td>
    <td align="right">7.66</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.63</td>
    <td align="right">11.97</td>
    <td align="right">15.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">11.94</td>
    <td align="right">14.37</td>
    <td align="right">8.98</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.60</td>
    <td align="right">7.48</td>
    <td align="right">8.24</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">19.76</td>
    <td align="right">18.47</td>
    <td align="right">17.53</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.14</td>
    <td align="right">7.16</td>
    <td align="right">4.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.25</td>
    <td align="right">12.62</td>
    <td align="right">17.00</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.87</td>
    <td align="right">4.32</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.91</td>
    <td align="right">5.69</td>
    <td align="right">5.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.53</td>
    <td align="right">17.85</td>
    <td align="right">17.79</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.99</td>
    <td align="right">4.80</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.69</td>
    <td align="right">8.54</td>
    <td align="right">8.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.76</td>
    <td align="right">21.55</td>
    <td align="right">16.90</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.68</td>
    <td align="right">5.35</td>
    <td align="right">5.35</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.42</td>
    <td align="right">11.32</td>
    <td align="right">11.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.20</td>
    <td align="right">27.46</td>
    <td align="right">17.65</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.00</td>
    <td align="right">5.98</td>
    <td align="right">6.00</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">18.40</td>
    <td align="right">14.52</td>
    <td align="right">14.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.41</td>
    <td align="right">4.00</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.02</td>
    <td align="right">5.32</td>
    <td align="right">5.33</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.93</td>
    <td align="right">5.65</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.93</td>
    <td align="right">4.92</td>
    <td align="right">4.13</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.36</td>
    <td align="right">6.06</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.37</td>
    <td align="right">8.78</td>
    <td align="right">8.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.07</td>
    <td align="right">7.20</td>
    <td align="right">5.47</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.38</td>
    <td align="right">6.75</td>
    <td align="right">6.86</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.34</td>
    <td align="right">10.73</td>
    <td align="right">10.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.04</td>
    <td align="right">7.14</td>
    <td align="right">5.42</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.50</td>
    <td align="right">7.47</td>
    <td align="right">7.51</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.06</td>
    <td align="right">12.73</td>
    <td align="right">13.68</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">51.79</td>
    <td align="right">22.49</td>
    <td align="right">9.81</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.96</td>
    <td align="right">13.91</td>
    <td align="right">18.19</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.49</td>
    <td align="right">5.36</td>
    <td align="right">5.09</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">11.24</td>
    <td align="right">7.32</td>
    <td align="right">7.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">45.12</td>
    <td align="right">34.40</td>
    <td align="right">27.01</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">12.72</td>
    <td align="right">8.20</td>
    <td align="right">9.03</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">20.13</td>
    <td align="right">17.29</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">72.44</td>
    <td align="right">83.23</td>
    <td align="right">26.51</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">24.11</td>
    <td align="right">19.28</td>
    <td align="right">19.53</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">39.87</td>
    <td align="right">30.57</td>
    <td align="right">27.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">89.68</td>
    <td align="right">106.12</td>
    <td align="right">29.41</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">24.10</td>
    <td align="right">21.35</td>
    <td align="right">24.43</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">49.54</td>
    <td align="right">38.53</td>
    <td align="right">36.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.05</td>
    <td align="right">4.65</td>
    <td align="right">4.91</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.79</td>
    <td align="right">5.97</td>
    <td align="right">6.10</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">10.16</td>
    <td align="right">6.65</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.41</td>
    <td align="right">9.91</td>
    <td align="right">6.53</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.27</td>
    <td align="right">9.00</td>
    <td align="right">14.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">26.72</td>
    <td align="right">16.94</td>
    <td align="right">16.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.09</td>
    <td align="right">20.86</td>
    <td align="right">15.21</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">23.24</td>
    <td align="right">20.18</td>
    <td align="right">23.72</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">41.66</td>
    <td align="right">30.60</td>
    <td align="right">31.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">17.38</td>
    <td align="right">25.20</td>
    <td align="right">18.79</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">28.31</td>
    <td align="right">23.77</td>
    <td align="right">25.53</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">44.97</td>
    <td align="right">31.52</td>
    <td align="right">28.04</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.58</td>
    <td align="right">30.63</td>
    <td align="right">15.41</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.30</td>
    <td align="right">41.62</td>
    <td align="right">36.21</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.45</td>
    <td align="right">15.91</td>
    <td align="right">15.92</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.12</td>
    <td align="right">20.47</td>
    <td align="right">20.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.88</td>
    <td align="right">63.07</td>
    <td align="right">38.71</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.23</td>
    <td align="right">19.35</td>
    <td align="right">19.36</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.17</td>
    <td align="right">26.59</td>
    <td align="right">26.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.78</td>
    <td align="right">77.65</td>
    <td align="right">38.10</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.32</td>
    <td align="right">18.43</td>
    <td align="right">18.40</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.81</td>
    <td align="right">33.13</td>
    <td align="right">33.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.42</td>
    <td align="right">96.32</td>
    <td align="right">36.91</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.18</td>
    <td align="right">18.84</td>
    <td align="right">18.78</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">35.09</td>
    <td align="right">37.52</td>
    <td align="right">37.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.56</td>
    <td align="right">13.60</td>
    <td align="right">13.53</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.13</td>
    <td align="right">19.68</td>
    <td align="right">19.70</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.46</td>
    <td align="right">22.08</td>
    <td align="right">22.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.80</td>
    <td align="right">15.93</td>
    <td align="right">15.91</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.06</td>
    <td align="right">18.63</td>
    <td align="right">18.59</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.33</td>
    <td align="right">28.85</td>
    <td align="right">28.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.47</td>
    <td align="right">19.35</td>
    <td align="right">19.35</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.07</td>
    <td align="right">18.26</td>
    <td align="right">18.27</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.48</td>
    <td align="right">45.63</td>
    <td align="right">45.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">23.26</td>
    <td align="right">25.43</td>
    <td align="right">25.50</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.94</td>
    <td align="right">19.98</td>
    <td align="right">19.96</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.27</td>
    <td align="right">55.27</td>
    <td align="right">55.26</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.09</td>
    <td align="right">105.94</td>
    <td align="right">21.04</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.84</td>
    <td align="right">42.94</td>
    <td align="right">39.54</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.40</td>
    <td align="right">16.86</td>
    <td align="right">16.24</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.49</td>
    <td align="right">21.50</td>
    <td align="right">22.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">39.88</td>
    <td align="right">70.96</td>
    <td align="right">45.80</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.65</td>
    <td align="right">23.34</td>
    <td align="right">23.72</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.66</td>
    <td align="right">40.84</td>
    <td align="right">43.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">63.44</td>
    <td align="right">131.60</td>
    <td align="right">53.36</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">26.91</td>
    <td align="right">28.06</td>
    <td align="right">30.83</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">55.55</td>
    <td align="right">63.93</td>
    <td align="right">61.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">150.15</td>
    <td align="right">191.11</td>
    <td align="right">57.80</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">36.06</td>
    <td align="right">33.24</td>
    <td align="right">35.04</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">59.27</td>
    <td align="right">76.02</td>
    <td align="right">80.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.76</td>
    <td align="right">13.85</td>
    <td align="right">13.78</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.59</td>
    <td align="right">19.98</td>
    <td align="right">20.10</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.71</td>
    <td align="right">23.09</td>
    <td align="right">23.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">13.36</td>
    <td align="right">16.91</td>
    <td align="right">17.06</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.96</td>
    <td align="right">21.83</td>
    <td align="right">21.48</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.23</td>
    <td align="right">42.85</td>
    <td align="right">33.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">24.09</td>
    <td align="right">30.75</td>
    <td align="right">27.74</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">25.27</td>
    <td align="right">22.67</td>
    <td align="right">24.24</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">82.06</td>
    <td align="right">62.65</td>
    <td align="right">62.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">44.61</td>
    <td align="right">54.50</td>
    <td align="right">57.20</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">34.14</td>
    <td align="right">34.78</td>
    <td align="right">33.40</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">97.87</td>
    <td align="right">76.49</td>
    <td align="right">71.64</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.21</td>
    <td align="right">10.43</td>
    <td align="right">7.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.93</td>
    <td align="right">22.98</td>
    <td align="right">26.64</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.57</td>
    <td align="right">12.40</td>
    <td align="right">12.45</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">13.00</td>
    <td align="right">16.04</td>
    <td align="right">16.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.59</td>
    <td align="right">35.06</td>
    <td align="right">29.23</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.15</td>
    <td align="right">14.09</td>
    <td align="right">14.13</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.35</td>
    <td align="right">22.49</td>
    <td align="right">22.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.97</td>
    <td align="right">47.39</td>
    <td align="right">30.31</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.80</td>
    <td align="right">15.52</td>
    <td align="right">15.56</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.01</td>
    <td align="right">32.16</td>
    <td align="right">32.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.64</td>
    <td align="right">60.32</td>
    <td align="right">31.09</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.61</td>
    <td align="right">16.39</td>
    <td align="right">16.37</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.84</td>
    <td align="right">37.02</td>
    <td align="right">37.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.05</td>
    <td align="right">9.40</td>
    <td align="right">9.41</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.79</td>
    <td align="right">13.95</td>
    <td align="right">13.93</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.28</td>
    <td align="right">16.71</td>
    <td align="right">16.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.92</td>
    <td align="right">14.16</td>
    <td align="right">14.01</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.63</td>
    <td align="right">15.45</td>
    <td align="right">15.47</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.36</td>
    <td align="right">22.29</td>
    <td align="right">22.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">12.81</td>
    <td align="right">17.58</td>
    <td align="right">17.66</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.74</td>
    <td align="right">16.88</td>
    <td align="right">16.78</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.73</td>
    <td align="right">30.82</td>
    <td align="right">30.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.19</td>
    <td align="right">22.05</td>
    <td align="right">22.05</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.01</td>
    <td align="right">17.86</td>
    <td align="right">17.92</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.00</td>
    <td align="right">35.90</td>
    <td align="right">35.96</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.14</td>
    <td align="right">46.62</td>
    <td align="right">10.72</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.23</td>
    <td align="right">22.75</td>
    <td align="right">28.35</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.67</td>
    <td align="right">12.59</td>
    <td align="right">12.56</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.03</td>
    <td align="right">16.72</td>
    <td align="right">16.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.73</td>
    <td align="right">35.31</td>
    <td align="right">30.04</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.54</td>
    <td align="right">15.34</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.24</td>
    <td align="right">22.16</td>
    <td align="right">22.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">26.20</td>
    <td align="right">48.89</td>
    <td align="right">30.86</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">15.73</td>
    <td align="right">16.43</td>
    <td align="right">16.46</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.42</td>
    <td align="right">38.27</td>
    <td align="right">38.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">43.63</td>
    <td align="right">83.05</td>
    <td align="right">37.74</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">17.82</td>
    <td align="right">21.53</td>
    <td align="right">19.63</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">33.82</td>
    <td align="right">44.44</td>
    <td align="right">51.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.21</td>
    <td align="right">9.47</td>
    <td align="right">9.46</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.93</td>
    <td align="right">14.06</td>
    <td align="right">14.02</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.38</td>
    <td align="right">17.64</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.14</td>
    <td align="right">14.96</td>
    <td align="right">14.44</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.17</td>
    <td align="right">15.76</td>
    <td align="right">15.40</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.77</td>
    <td align="right">23.91</td>
    <td align="right">25.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">12.92</td>
    <td align="right">18.83</td>
    <td align="right">17.95</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.64</td>
    <td align="right">16.63</td>
    <td align="right">16.85</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">28.52</td>
    <td align="right">31.68</td>
    <td align="right">31.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">19.58</td>
    <td align="right">32.95</td>
    <td align="right">38.40</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">18.58</td>
    <td align="right">21.45</td>
    <td align="right">20.86</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">35.91</td>
    <td align="right">37.98</td>
    <td align="right">38.21</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">46.28</td>
    <td align="right">9.23</td>
    <td align="right">8.44</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">56.58</td>
    <td align="right">53.79</td>
    <td align="right">37.04</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.26</td>
    <td align="right">17.48</td>
    <td align="right">20.65</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">20.03</td>
    <td align="right">41.60</td>
    <td align="right">41.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">85.19</td>
    <td align="right">78.21</td>
    <td align="right">38.37</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.47</td>
    <td align="right">18.96</td>
    <td align="right">20.66</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.00</td>
    <td align="right">56.85</td>
    <td align="right">57.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">106.16</td>
    <td align="right">96.69</td>
    <td align="right">37.45</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.70</td>
    <td align="right">19.47</td>
    <td align="right">20.60</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.71</td>
    <td align="right">77.22</td>
    <td align="right">77.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">135.44</td>
    <td align="right">122.24</td>
    <td align="right">38.27</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.71</td>
    <td align="right">20.44</td>
    <td align="right">21.24</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">42.04</td>
    <td align="right">91.52</td>
    <td align="right">94.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.21</td>
    <td align="right">23.98</td>
    <td align="right">23.60</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.73</td>
    <td align="right">22.44</td>
    <td align="right">25.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.04</td>
    <td align="right">41.42</td>
    <td align="right">40.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.09</td>
    <td align="right">32.72</td>
    <td align="right">24.10</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.84</td>
    <td align="right">24.17</td>
    <td align="right">25.71</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.97</td>
    <td align="right">56.96</td>
    <td align="right">56.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.51</td>
    <td align="right">54.94</td>
    <td align="right">39.18</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">26.65</td>
    <td align="right">26.66</td>
    <td align="right">27.09</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">42.27</td>
    <td align="right">76.55</td>
    <td align="right">79.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">25.24</td>
    <td align="right">53.05</td>
    <td align="right">36.54</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.25</td>
    <td align="right">28.78</td>
    <td align="right">29.32</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">47.41</td>
    <td align="right">94.16</td>
    <td align="right">93.90</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">68.61</td>
    <td align="right">37.55</td>
    <td align="right">12.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">62.83</td>
    <td align="right">57.96</td>
    <td align="right">41.12</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">20.75</td>
    <td align="right">18.88</td>
    <td align="right">25.81</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.18</td>
    <td align="right">46.02</td>
    <td align="right">45.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">103.51</td>
    <td align="right">92.33</td>
    <td align="right">43.74</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">35.88</td>
    <td align="right">27.33</td>
    <td align="right">29.12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">36.48</td>
    <td align="right">75.27</td>
    <td align="right">74.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">209.61</td>
    <td align="right">137.32</td>
    <td align="right">45.85</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">29.59</td>
    <td align="right">24.12</td>
    <td align="right">24.94</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.15</td>
    <td align="right">83.62</td>
    <td align="right">82.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">212.62</td>
    <td align="right">200.48</td>
    <td align="right">49.05</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">40.27</td>
    <td align="right">29.16</td>
    <td align="right">29.50</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">50.49</td>
    <td align="right">103.51</td>
    <td align="right">104.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.86</td>
    <td align="right">28.89</td>
    <td align="right">28.77</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.17</td>
    <td align="right">24.47</td>
    <td align="right">27.75</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.39</td>
    <td align="right">41.95</td>
    <td align="right">42.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">16.75</td>
    <td align="right">44.32</td>
    <td align="right">32.17</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.61</td>
    <td align="right">28.51</td>
    <td align="right">31.56</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">34.72</td>
    <td align="right">62.41</td>
    <td align="right">65.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">31.78</td>
    <td align="right">74.66</td>
    <td align="right">52.81</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">36.58</td>
    <td align="right">40.05</td>
    <td align="right">35.15</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">48.55</td>
    <td align="right">80.08</td>
    <td align="right">83.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">39.24</td>
    <td align="right">88.09</td>
    <td align="right">58.06</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">39.17</td>
    <td align="right">47.42</td>
    <td align="right">42.52</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">60.89</td>
    <td align="right">110.61</td>
    <td align="right">108.30</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
